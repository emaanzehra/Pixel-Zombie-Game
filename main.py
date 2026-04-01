import random
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# --- NEW GAME STATE WITH HEALTH ---
def get_initial_state():
    return {
        "hp": 100,
        "max_hp": 100,
        "total_kills": 0,
        "player_level": 1,
        "inventory": [],
        "status": "Alive" # Can become "Dead"
    }

game_stats = get_initial_state()

LOOT_TABLE = {
    "Common": ["Rusty Knife", "Bandage"],
    "Rare": ["Kevlar Vest", "Medkit"],
    "Legendary": ["Zombie Antidote", "M4A1-S"]
}

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/hunt")
def hunt_monster(use_luck_charm: bool = False):
    if game_stats["status"] == "Dead":
        return {"message": "You are dead! Reset the game.", "state": game_stats}

    # 1. Zombie Fights Back! (Damage scales with your level)
    damage_taken = random.randint(5, 15) * game_stats["player_level"]
    
    # Kevlar Vest reduces damage
    if "Kevlar Vest" in game_stats["inventory"]:
        damage_taken = int(damage_taken * 0.5) 
        
    game_stats["hp"] -= damage_taken

    # 2. Check if you died
    if game_stats["hp"] <= 0:
        game_stats["hp"] = 0
        game_stats["status"] = "Dead"
        return {"message": f"KILLED by a zombie. You survived {game_stats['total_kills']} kills.", "state": game_stats}

    # 3. If you survive, you get the kill and loot
    game_stats["total_kills"] += 1
    if game_stats["total_kills"] % 5 == 0:
        game_stats["player_level"] += 1

    roll = random.randint(1, 100)
    if use_luck_charm: roll += 20

    rarity = "Legendary" if roll > 90 else "Rare" if roll > 60 else "Common"
    item = random.choice(LOOT_TABLE[rarity])
    game_stats["inventory"].append(item)

    return {
        "message": f"Zombie Slain! You took {damage_taken} damage.",
        "item": item,
        "rarity": rarity,
        "state": game_stats
    }

@app.post("/heal")
def heal_player():
    if game_stats["status"] == "Dead":
        return {"message": "Too late, you're dead.", "state": game_stats}

    if "Medkit" in game_stats["inventory"]:
        game_stats["hp"] = min(game_stats["hp"] + 50, game_stats["max_hp"])
        game_stats["inventory"].remove("Medkit")
        return {"message": "Used Medkit! (+50 HP)", "state": game_stats}
    
    elif "Bandage" in game_stats["inventory"]:
        game_stats["hp"] = min(game_stats["hp"] + 20, game_stats["max_hp"])
        game_stats["inventory"].remove("Bandage")
        return {"message": "Used Bandage! (+20 HP)", "state": game_stats}
    
    return {"message": "No healing items in inventory!", "state": game_stats}

@app.post("/reset")
def reset_game():
    global game_stats
    game_stats = get_initial_state()
    return {"message": "Game Reset. Good luck.", "state": game_stats}