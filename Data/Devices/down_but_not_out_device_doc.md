# Down But Not Out Device (DBNO Device) – UEFN Verse Device Documentation

## 🔹 Description
The `down_but_not_out_device` (DBNO device) lets you control the "Down But Not Out" state—where a player is incapacitated but not eliminated—in your Fortnite island. This device enables or disables DBNO, configures recovery and revive options, and exposes events for custom scripting (such as tracking downs, revives, pickups, or shake downs), allowing rich team-based and squad gameplay mechanics.

## 🧱 Imports Required
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /Fortnite.com/Characters }
```

## 🔗 Inheritance Hierarchy
- **creative_object**: Base class for creative devices and props.
- **creative_device_base**: Base class for creative_device.
- **down_but_not_out_device**

## 🧹 Core Events & Methods
| Name / Function        | Type / Signature        | Description                                                |
|------------------------|--------------------------|------------------------------------------------------------|
| AgentDownedEvent       | listenable(agent)        | Fires when an agent enters the DBNO (downed) state.        |
| AgentPickedUpEvent     | listenable(agent)        | Agent in DBNO state is picked up (carried).                |
| AgentDroppedEvent      | listenable(agent)        | Agent in DBNO state is dropped from being carried.         |
| AgentThrownEvent       | listenable(agent)        | Agent in DBNO state is thrown by another agent.            |
| AgentRevivedEvent      | listenable(agent)        | Agent has been revived.                                    |
| ShakeDownEvent         | listenable(agent)        | Fires for aggressor performing a shake down.               |
| ShakenDownEvent        | listenable(agent)        | Fires for victim of a shake down.                          |
| Enable()               | void                     | Enables this device (DBNO functionality).                  |
| Disable()              | void                     | Disables this device.                                      |
| Down(Agent)            | void                     | Sets specified agent to DBNO state.                        |
| Revive(Agent)          | void                     | Sets specified agent back to "Healthy" from DBNO.          |

## 🎛 Configuration Options (Details Panel)
| Option                   | Values                                     | Description                                      |
|--------------------------|---------------------------------------------|--------------------------------------------------|
| DBNO Enabled             | Do Not Override, Yes, No                   | If DBNO can occur for players                   |
| Tenacity Type/Amount     | Default, Max Health, Custom / Number        | DBNO HP pool (min 1; custom value possible)     |
| Tenacity Depletion Rate  | Default, Custom / Number                    | Health lost per second while downed             |
| Allow Revives            | Yes, No                                     | Whether agents can be revived                   |
| Time to Revive           | Seconds, Instant                            | Duration for revive action                      |
| Revive Progress Decay    | Battle Royale, Instant Reset, Custom Decay  | How revive progress decays                      |
| Shakedowns               | On, Off                                     | Enable/disable shakedown mechanic while DBNO    |
| Health After Revive      | % of Max Health                             | How much HP a player regains upon revive        |

> **Note:** Configure all options via the UEFN Details panel.

## 🛠️ Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Fortnite.com/Characters }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Device to manage DBNO state

    dbno_example := class(creative_device):

        @editable
        DBNODevice : down_but_not_out_device = down_but_not_out_device{}

        @editable
        ReviveButton : button_device = button_device{}

        OnBegin<override>()<suspends> : void =
            # Subscribe to DBNO events
            DBNODevice.AgentDownButNotOutEvent.Subscribe(OnPlayerDowned)
            DBNODevice.AgentRevivedEvent.Subscribe(OnPlayerRevived)

            # Subscribe to revive button
            ReviveButton.InteractedWithEvent.Subscribe(OnReviveButtonPressed)

        # Event handlers
        OnPlayerDowned(Agent : agent) : void =
            Print("Player downed!")

        OnPlayerRevived(Agent : agent) : void =
            Print("Player revived!")

        # Revive button handler
        OnReviveButtonPressed(Agent : agent) : void =
            if (Character := Agent.GetFortCharacter[]):
                if (Character.IsDownButNotOut[]):
                    DBNODevice.Revive(Agent)
                    Print("Player revived via button!")
```

### Explanation:
- Subscribe to DBNO device events (downed, revived) to trigger custom game logic, achievement tracking, or notifications.
- Versatile APIs allow you to programmatically force-down or revive players (e.g., for custom hazards, traps, or puzzles).
- Pair with team, class, or elimination logic for advanced squad gameplay.

## 🧠 Best Practices
- Configure device options in the Details panel to suit your “downed” and “revive” flow (tenacity, revive time, etc.).
- Subscribe to DBNO events (for score, tracking, analytics, or VFX).
- Only use `Down()` and `Revive()` with valid **agent** objects (never with plain player or character references).
- Use `Enable()`/`Disable()` to control DBNO for specific rounds, zones, or modes.
- Calibrate tenacity and revive settings for your intended challenge and pacing.

## ❌ Incorrect Usage Examples and Fixes
| Issue                       | ❌ Wrong Example          | ✅ Correct Example          | Explanation                             |
|----------------------------|------------------------------|-------------------------------|-----------------------------------------|
| Using `Down()` on player   | `DBNODevice.Down(Player)`    | `DBNODevice.Down(Agent)`      | Must use agent, not player/character    |
| Not assigning @editable    | No Details assignment        | Assign device in Details panel | Avoids nil/error on reference in Verse  |
| Skipping `Enable()`        | Expecting it to work when disabled | Call `Enable()` first         | Device must be enabled to function      |

> **Note:**
- DBNO state requires **teams to be enabled** in island/game settings.
- Use DBNO with revive for team-based, Battle Royale, or rescue-focused gameplay.
- Events allow deep customization for UI, narrative, analytics, and more.

