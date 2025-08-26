# Team Settings and Inventory Device Documentation (UEFN - Verse)

## 📙 Description

The `team_settings_and_inventory_device` enables advanced customization of team settings and inventory rules in Fortnite's Unreal Editor for Fortnite (UEFN). This device overrides the default My Island team/inventory setup, allowing developers to configure health, shields, classes, item loadouts, respawn rules, and more per team. It is ideal for class-based or asymmetric team mechanics and custom game loops.

## 🧱 Verse Using Statement

```verse
verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy

- `creative_object`
- `creative_device_base`
- `team_settings_and_inventory_device`

## 🛠️ Key Functions & Methods

| Name                        | Description                                                          |
| --------------------------- | -------------------------------------------------------------------- |
| `EndRound()`                | Ends the round and declares this team as the winner.                 |
| `GetTeamMembers()`          | Returns an array of agents currently on this device's assigned team. |
| `IsOnTeam(agent)`           | Checks if the given agent is on this device's assigned team.         |
| `GetTransform()`            | Retrieves the device’s transform (position, rotation, scale).        |
| `MoveTo()` / `TeleportTo()` | Moves or teleports the device to a new location.                     |

## 🧍 Events (Data Members)

| Event Name                  | Type                  | Description                                           |
| --------------------------- | --------------------- | ----------------------------------------------------- |
| `EnemyEliminatedEvent`      | `listenable(agent)`   | Fires when a member of this team eliminates an enemy. |
| `TeamMemberEliminatedEvent` | `listenable(agent)`   | Fires when a team member is eliminated.               |
| `TeamOutOfRespawnsEvent`    | `listenable(tuple())` | Fires when the team runs out of respawns.             |
| `TeamMemberSpawnedEvent`    | `listenable(agent)`   | Fires when a team member spawns.                      |

## 🎛 Configuration Options (Details Panel)

| Option                        | Description                                                |
| ----------------------------- | ---------------------------------------------------------- |
| Team Name/Description         | Set a custom name and description for the team.            |
| Team                          | Assigns which team this device's settings affect.          |
| Team Color & Icon             | Customizes team color and icon appearance.                 |
| Default Class Identifier      | Sets a default class for the team.                         |
| Max Health / Shields          | Overrides max health and shield values.                    |
| Grant Items on Respawn        | Enables loadout granting on player respawn.                |
| Grant Condition               | Choose between "Always" or "Only When Inventory is Empty". |
| On-Grant Behavior             | Option to clear inventory or keep existing items.          |
| Equip Granted Item            | Selects which item to auto-equip first.                    |
| Initial/Spare Weapon Ammo     | Sets ammo count when players spawn or respawn.             |
| Score/Resource on Elimination | Grants score/gold/material for enemy eliminations.         |

> Note: Additional options may be revealed based on other enabled settings.

## 🛠️ Verse Usage Example

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

team_settings_example := class(creative_device):

    @editable
    TeamDevice : team_settings_and_inventory_device = team_settings_and_inventory_device{}

    OnBegin<override>()<suspends> : void =
        # Subscribe to key team events
        TeamDevice.EnemyEliminatedEvent.Subscribe(OnEnemyEliminated)
        TeamDevice.TeamMemberEliminatedEvent.Subscribe(OnTeamMemberEliminated)
        TeamDevice.TeamOutOfRespawnsEvent.Subscribe(OnOutOfRespawns)

    # Handle when a team member eliminates an enemy
    OnEnemyEliminated(Agent : agent) : void =
        Print("A member of this team eliminated an enemy! Awarding bonus.")
        # Example: award extra score, grant items, etc.

    # Handle when a team member is eliminated
    OnTeamMemberEliminated(Agent : agent) : void =
        Print("A team member was eliminated!")

    # Handle all respawns lost
    OnOutOfRespawns() : void =
        Print("Team out of respawns! Ending round.")
        TeamDevice.EndRound()
```

## 📖 How to Use in UEFN

1. **Place Device(s)**

   - Add one `team_settings_and_inventory_device` for each team.
   - Set unique team #, name, class, and loadout configurations in the Details panel.

2. **Combine with Class Designer or Item Granter (Optional)**

   - Use Class Designer for more granular class settings per team.

3. **Create & Build Verse Device**

   - In Verse Explorer: Right-click a folder → Create New Verse File (e.g., `team_settings_example.verse`).
   - Select *Create Empty*, paste sample code, and save.
   - Build the code: `Verse → Build Verse Code` or `Ctrl+Shift+B`.

4. **Assign References**

   - Place your custom Verse device in the world.
   - Set the `TeamDevice` reference to your specific team settings device in Details.

5. **Test and Iterate**

   - Run simulations to test different team loadouts, respawns, eliminations, and win conditions.

## 🧠 Tips

- **Device hierarchy precedence:**
  1. My Island (global)
  2. Team Settings & Inventory (per-team)
  3. Class Designer (per-class, overrides team settings)
- Use `GetTeamMembers()` to dynamically manage or monitor team composition.
- Leverage events for advanced logic: rewards, stats tracking, round control.

## ❌ Common Issues & Fixes

| Issue                       | Cause                           | Solution                                    |
| --------------------------- | ------------------------------- | ------------------------------------------- |
| Team setups not applied     | Device not linked or team unset | Assign correct team and configure overrides |
| Event handlers not firing   | Not subscribed via Verse        | Use `.Subscribe()` for desired events       |
| Members not getting loadout | Loadout grant option disabled   | Enable "Grant Items on Respawn"             |

## ⚠️ Notes

- Place separate devices for each team to ensure correct custom settings.
- Combine with other devices (Score Manager, Class Designer, etc.) for full game logic.
- Some advanced options in Details panel are shown based on current settings (contextual filtering).

