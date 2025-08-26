# Prop-o-Matic Manager Device – UEFN Verse Device Documentation

## 🔹 Description

The `prop_o_matic_manager_device` is used to customize how the Prop-o-Matic weapon behaves and how the game reacts to players using it. This manager controls periodic pings of hidden prop players, health scaling based on prop size, prop disguise cancel rules, prop HUD, and direct events when players enter or leave disguise. **Only one instance should be placed per island** for proper functionality.

## 🧱 Verse Using Statement

```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy

- `creative_object`
- `creative_device_base`
- `prop_o_matic_manager_device`

## 🧩 Events (Data Members)

| Name                        | Type              | Description                                       |
| --------------------------- | ----------------- | ------------------------------------------------- |
| BeginEnteringDisguiseEvent  | listenable(agent) | Fires when an agent starts entering a disguise.   |
| FinishEnteringDisguiseEvent | listenable(agent) | Fires when an agent finishes entering a disguise. |
| ExitingDisguiseEvent        | listenable(agent) | Fires when an agent exits a disguise.             |

## 🛠️ Functions & Methods

| Name                             | Description                                                    |
| -------------------------------- | -------------------------------------------------------------- |
| `PingPlayerProps()`              | Pings all agents currently disguised as props.                 |
| `PingPlayerProp(agent)`          | Pings a specific player if currently disguised as a prop.      |
| `SetPingFrequency(float)`        | Sets interval (in seconds) between auto pings of hidden props. |
| `SetPingProps(logic)`            | Enables/disables periodic pings of hidden props.               |
| `SetShowPropsRemaining(logic)`   | Shows/hides count of prop players on HUD.                      |
| `SetShowPropPingCooldown(logic)` | Shows/hides cooldown timer on HUD.                             |
| `IsPlayerProp(agent)<decides>`   | Returns true if the agent is currently disguised as a prop.    |

## 📂 Configuration Options (Details Panel)

| Option                         | Description                                             |
| ------------------------------ | ------------------------------------------------------- |
| Ping Hidden Props On Interval  | Enables pings for hidden props on a timer.              |
| Prop Ping Frequency            | Interval in seconds (default: 15).                      |
| Should Show Props Remaining    | Show count of remaining props on HUD.                   |
| Allow Disguise To Be Canceled  | Let players cancel disguises manually.                  |
| Allow Changing Disguises       | Let players change props without revealing.             |
| Prop Health Behavior           | Option to scale health with prop size.                  |
| Equip Pickaxe After Cancelling | Auto-equip pickaxe after disguise cancel.               |
| Show Prop Ping Countdown       | Show ping countdown on HUD.                             |
| Drop Prop-O-Matic Behavior     | Control what happens to weapon upon player elimination. |
| Disguise Animation Duration    | Set how long disguise entry animation takes.            |

## 🧩 Events Overview

| Event                       | When It Fires                           |
| --------------------------- | --------------------------------------- |
| BeginEnteringDisguiseEvent  | When player starts disguising as prop   |
| FinishEnteringDisguiseEvent | When player successfully becomes a prop |
| ExitingDisguiseEvent        | When player leaves a prop disguise      |

## 🪠 Verse Usage Example

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

prop_o_matic_example := class(creative_device):

    @editable
    PropManager : prop_o_matic_manager_device = prop_o_matic_manager_device{}

    @editable
    TogglePingButton : button_device = button_device{}

    @editable
    ToggleHUDButton : button_device = button_device{}

    var PingEnabled : logic = false
    var HUDEnabled : logic = false

    OnBegin<override>()<suspends> : void =
        PropManager.BeginEnteringDisguiseEvent.Subscribe(OnBeginDisguise)
        PropManager.FinishEnteringDisguiseEvent.Subscribe(OnFinishDisguise)
        PropManager.ExitingDisguiseEvent.Subscribe(OnExitDisguise)

        TogglePingButton.InteractedWithEvent.Subscribe(OnTogglePing)
        ToggleHUDButton.InteractedWithEvent.Subscribe(OnToggleHUD)

    OnBeginDisguise(Agent : agent) : void =
        Print("Player started entering disguise")

    OnFinishDisguise(Agent : agent) : void =
        Print("Player finished entering disguise")

    OnExitDisguise(Agent : agent) : void =
        Print("Player exited disguise")

    OnTogglePing(Agent : agent) : void =
        if (PingEnabled?):
            set PingEnabled = false
            Print("Prop ping disabled")
        else:
            set PingEnabled = true
            Print("Prop ping enabled")

    OnToggleHUD(Agent : agent) : void =
        if (HUDEnabled?):
            set HUDEnabled = false
            Print("Props remaining HUD hidden")
        else:
            set HUDEnabled = true
            Print("Props remaining HUD shown")

    PingAllProps() : void =
        PropManager.PingPlayerProps()

    SetPingFrequency(Frequency : float) : void =
        PropManager.SetPingFrequency(Frequency)
```

### Explanation

- Use `@editable` references for the Prop-o-Matic manager and buttons.
- Subscribes to disguise events and prints messages to the Output Log.
- Button presses toggle HUD and ping states.
- `PingAllProps()` and `SetPingFrequency()` are utility functions that can be reused.

## 👩‍🏫 How to Set Up in UEFN

1. **Place the Device**

   - Add one `prop_o_matic_manager_device` to the world.
   - Set up configuration options in the Details panel.

2. **Add Control Devices (Recommended)**

   - Add two `button_device`s for toggling pings and HUD visibility.

3. **Create & Build Verse Device**

   - In Verse Explorer, create a new file (e.g., `prop_o_matic_example.verse`).
   - Paste the code, save, and press **Ctrl+Shift+B** to build.

4. **Assign Device References**

   - Drag your Verse device into the level.
   - Link `PropManager`, `TogglePingButton`, and `ToggleHUDButton` via Details.

5. **Test and Adjust**

   - Playtest your level and interact with the buttons.
   - Watch Output Log for disguise events.

## 🧠 Best Practices

- Only one Prop-o-Matic Manager per island.
- Use Verse events for scoring, logic, or custom gameplay.
- Classic Prop Hunt: enable regular pings + show props remaining.
- Use `SetPingFrequency()` to adjust difficulty dynamically.

## ❌ Common Issues & Fixes

| Issue                    | Problem                         | Fix                                                   |
| ------------------------ | ------------------------------- | ----------------------------------------------------- |
| Multiple managers placed | More than one manager device    | Place only one `prop_o_matic_manager_device`          |
| No reactions in Verse    | Events not subscribed           | Use `.Subscribe()` for all required events            |
| Pings/HUD not updating   | Logic not toggled properly      | Recheck Verse code logic and ensure wiring is correct |
| @editable blank fields   | Devices not assigned in Details | Assign all `@editable` fields in the Details panel    |

---

**Note**: The Prop-o-Matic manager is essential for Prop Hunt-style gameplay, controlling disguise behavior, prop visibility, HUD feedback, and more. Many core settings are defined in the Details panel, while advanced behavior can be customized through Verse logic.

