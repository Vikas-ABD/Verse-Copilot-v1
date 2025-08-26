📘 signal_remote_manager_device – UEFN Verse Device Documentation

🔹 Description:
The signal_remote_manager_device is used to trigger custom in-game responses when a player sends a Primary or Secondary signal using a Signal Remote item (A, B, C, D). This allows remote-controlled actions such as opening doors, activating devices, or executing Verse logic. Each device supports one remote type (A-D).

🧱 Verse Using Statement:
```verse
using { /Fortnite.com/Devices }
```

🔗 Inheritance Hierarchy:
* creative_object
* creative_device_base
* signal_remote_manager_device (concrete, final)

🧩 Data Members (Events):
| Name                | Type                | Description                                                  |
|---------------------|---------------------|--------------------------------------------------------------|
| PrimarySignalEvent  | listenable(agent)   | Fires when a player triggers Primary signal (e.g. left-click) |
| SecondarySignalEvent| listenable(agent)   | Fires when a player triggers Secondary signal (e.g. right-click)|

🛠️ Functions & Methods:
| Function Name | Description |
|---------------|-------------|
| Disable       | Disables this device |
| Enable        | Enables this device |
| GetTransform  | Returns the transform of the creative_object in cm (check IsValid first) |
| MoveTo        | Moves object to a given Position & Rotation or Transform over time |
| TeleportTo    | Instantly moves object to a given Position & Rotation or Transform |

🎛 Configuration Options (Details Panel):
| Option                         | Description |
|-------------------------------|-------------|
| Cooldown Time                 | Delay between remote signal activations per player |
| On Primary Activation Transmit On | Sends event on Primary signal |
| On Secondary Fire Transmit On | Sends event on Secondary signal |
| Activate on Enable            | Device becomes active when enabled in-game |
| Signal Remote Item            | Choose A/B/C/D remote type (ensure player is given matching remote) |

🧰 Usage Example in Verse:
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

signal_remote_manager_example := class(creative_device):
    @editable
    SignalManager : signal_remote_manager_device = signal_remote_manager_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        SignalManager.PrimarySignalEvent.Subscribe(OnPrimarySignal)
        SignalManager.SecondarySignalEvent.Subscribe(OnSecondarySignal)

        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    OnPrimarySignal(Agent : agent) : void =
        Print("Primary signal received from agent!")

    OnSecondarySignal(Agent : agent) : void =
        Print("Secondary signal received from agent!")

    OnEnablePressed(Agent : agent) : void =
        SignalManager.Enable()
        Print("Signal manager enabled!")

    OnDisablePressed(Agent : agent) : void =
        SignalManager.Disable()
        Print("Signal manager disabled!")
```

✅ How to Use in UEFN:
1. **Place Devices**: Add a signal_remote_manager_device and optional control buttons.
2. **Assign Remotes**: Choose A/B/C/D in the Details panel and configure cooldowns and channels.
3. **Give Remotes to Players**: Use Class Designer, Item Granter, or Item Spawner. Set "Equip Granted Item" to "First Item".
4. **Customize Responses**: Use Verse subscriptions or UEFN channels to wire Primary/Secondary signals to actions.

🧠 Best Practices:
* One signal_remote_manager_device per remote type.
* Use cooldowns to avoid spamming.
* Always grant the correct remote to players.
* Use Verse logic for advanced control and event chaining.

❌ Common Mistakes & Fixes:
| Issue                     | ❌ Wrong Usage                       | ✅ Correct Usage                                    | Explanation |
|--------------------------|--------------------------------------|---------------------------------------------------|-------------|
| No signal reaction       | Players not given remote             | Use item granter/class designer to provide remote | Players must hold remote |
| Mismatched signal type   | Device set to A, item is B           | Match remote type with manager                    | A-D remotes are separate |
| Events not handled       | No Verse/channel wiring              | Use event hooks or UEFN channels                  | Must explicitly handle events |
| Signal spamming          | Cooldown too low                     | Set reasonable cooldown                           | Prevents gameplay lag and abuse |

📌 Note:
Use Verse subscriptions for deeper control over game mechanics such as custom unlocks, player progression, or triggering multiple devices. Combine this device with triggers, animations, VFX, and puzzles for immersive gameplay.

