# npc_spawner_device

## Overview

**Purpose**: The `npc_spawner_device` spawns and manages NPCs defined by Character Definition assets. These can include custom characters, guards, wildlife, or Verse-driven behaviors.

**Configuration**: In the Details panel of the device, you can assign a Character Definition and configure modifiers for custom behaviors, health, inventory, AI behavior, team, and more.

---

## Key Methods & Events

| Method         | Description                                                               |
|----------------|---------------------------------------------------------------------------|
| `Enable()`     | Enables the spawner; NPCs begin spawning (automatically or by script)      |
| `Disable()`    | Disables the device; despawns all NPCs if "Despawn AIs When Disabled" is on |
| `Spawn()`      | Immediately attempts to spawn a new NPC                                    |
| `Reset()`      | Resets the spawn count; allows spawning a new batch of NPCs               |
| `DespawnAll(?agent)` | Instantly eliminates all spawned NPCs; credit to provided agent (optional) |

### Events

| Event            | When It Fires                                 |
|------------------|-----------------------------------------------|
| `SpawnedEvent`    | Fires when an NPC is spawned; returns new agent |
| `EliminatedEvent` | Fires when an NPC is eliminated (requires extra setup) |

---

## Complete Verse Example

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }
using { /Fortnite.com/Game }

npc_spawner_example := class(creative_device):

    @editable
    NPCSpawner : npc_spawner_device = npc_spawner_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    SpawnButton : button_device = button_device{}

    @editable
    ResetButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        # Subscribe to NPC events
        NPCSpawner.SpawnedEvent.Subscribe(OnNPCSpawned)

        # Subscribe to control buttons
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        SpawnButton.InteractedWithEvent.Subscribe(OnSpawnPressed)
        ResetButton.InteractedWithEvent.Subscribe(OnResetPressed)

    # Event handlers
    OnNPCSpawned(Agent : agent) : void =
        Print("NPC spawned!")

    # Button control handlers
    OnEnablePressed(Agent : agent) : void =
        NPCSpawner.Enable()
        Print("NPC spawner enabled!")

    OnDisablePressed(Agent : agent) : void =
        NPCSpawner.Disable()
        Print("NPC spawner disabled!")

    OnSpawnPressed(Agent : agent) : void =
        NPCSpawner.Spawn()
        Print("NPC spawned via button!")

    OnResetPressed(Agent : agent) : void =
        NPCSpawner.Reset()
        Print("NPC spawner reset!")
```

---

## Instructions to Use in UEFN

### 1. Place Devices in Level
- Add an `npc_spawner_device` to your world.
- Add four `button_device` devices (label them Enable, Disable, Spawn, Reset).

### 2. Configure NPC Spawner in Details Panel
- Assign an NPC Character Definition (or create a custom one).
- Set:
  - "Spawn Count"
  - "Enabled at Start"
  - "Despawn AIs When Disabled"
  - Team, patrol path, and modifiers

### 3. Create and Add Verse Script
- Open Verse Explorer (Top Menu → Verse → Verse Explorer).
- Right-click a folder → Create New Verse File (e.g., `npc_spawner_example.verse`).
- Paste the code above and save.
- Click Verse → Build Verse Code (or Ctrl+Shift+B).

### 4. Assign Editable References
- In the Verse device's Details panel:
  - Assign all four button devices.
  - Assign the placed `npc_spawner_device`.

### 5. Test in Play Session
- Use the Enable/Disable/Spawn/Reset buttons to control NPC logic.
- Monitor the output log for spawn events or interactions.

---

## Tips & Best Practices

- Use `EliminatedEvent` (with extra setup) to handle score tracking or progression logic.
- `Reset()` enables fresh spawn waves, ideal for rounds.
- Assign teams, inventory, effects, or custom logic via Character Definition.
- Use `DespawnAll(?agent)` to assign elimination credit to a player agent.

---

## Common Issues & Solutions

| Issue                      | Problem                                       | Solution                                                       |
|----------------------------|-----------------------------------------------|----------------------------------------------------------------|
| NPCs not spawning         | Device not enabled or no Character Definition | Call `.Enable()` and assign Character Definition               |
| Events not firing         | No event subscription                        | Add `.Subscribe(...)` in `OnBegin`                             |
| NPCs not eliminated       | "Despawn AIs When Disabled" is off           | Enable this option in the Details panel                        |
| Editable references broken| Missing @editable setup                      | Set all references properly in Details & rebuild Verse         |

---

## Final Notes
- All advanced configurations (inventory, awareness, paths, modifiers) are controlled via the Character Definition asset and device settings.
- Blend device behavior and Verse logic for complete control over spawning, waves, missions, escort or boss gameplay.

