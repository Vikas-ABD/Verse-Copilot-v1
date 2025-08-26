# Bank Vault Device – UEFN Verse Device Documentation

## 🔍 Description
The `bank_vault_device` is a customizable vault door mechanic in Unreal Editor for Fortnite (UEFN), tailored for heist or break-in gameplay. It allows players or triggered events to begin a vault opening sequence, which involves damaging a configurable set of weakpoints. These weakpoints become sequentially active, glow when activated, and are made vulnerable to damage before the vault can be opened. The device is flexible, supporting class/team restrictions and fully programmable using Verse.

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `bank_vault_device` (implements `enableable`)

## 🛠️ Key Methods & Functions
| Method | Description |
|--------|-------------|
| `Enable()` | Enables the device and prepares it for interaction. |
| `Disable()` | Disables and pauses all interaction and weakpoint damage. |
| `IsEnabled()` | Returns `true` if the device is enabled. |
| `StartSequence()` | Begins or resumes the vault opening sequence. |
| `PauseSequence()` | Freezes current progress and disables weakpoint vulnerability. |
| `ForceOpen()` | Instantly opens the vault by destroying all weakpoints. |
| `Reset()` | Restores the vault to its initial state and heals all weakpoints. Must be enabled first. |
| `IsSequenceActive()` | Returns `true` if the sequence is currently active and unpaused. |

## 🧹 Events (Data Members)
| Name | Type | Description |
|------|------|-------------|
| `StartSequenceEvent` | `listenable(?agent)` | Fires when the vault opening sequence begins. |
| `OpenEvent` | `listenable(?agent)` | Fires when the vault is successfully opened. |
| `ActivateWeakpointEvent` | `listenable(tuple(?agent, int))` | Fires when a weakpoint is activated. |
| `WeakpointVulnerableEvent` | `listenable(tuple(?agent, int))` | Fires when a weakpoint becomes vulnerable. |
| `DestroyWeakpointEvent` | `listenable(tuple(?agent, int))` | Fires when a weakpoint is destroyed. |

## 🎮 Device Configuration (Details Panel)
| Option | Description |
|--------|-------------|
| Enabled at Game Start | Toggles vault activation at the start. Default: On. |
| Require Thermite | Restricts vault opening to agents with thermite. |
| Activating Team/Class | Restricts which players can interact. |
| Weakpoints Take External Damage | Allow weapons to damage weakpoints. |
| Weakpoint Health | Amount of damage required per weakpoint. Default: 750. |
| Number of Weakpoints | Select between 1 to 5. Default: 5. |
| Passive Damage Per Second | Damage over time to weakpoints. Optional. |
| Zone Dimensions | Customize the vault's player-facing interaction zone. |
| Show Progress Zone, Map Icon | Toggle UI and map visibility. |

## 🛠️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

bank_vault_example := class(creative_device):

    @editable
    VaultDevice : bank_vault_device = bank_vault_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    StartSequenceButton : button_device = button_device{}

    @editable
    PauseSequenceButton : button_device = button_device{}

    @editable
    ForceOpenButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        StartSequenceButton.InteractedWithEvent.Subscribe(OnStartSequencePressed)
        PauseSequenceButton.InteractedWithEvent.Subscribe(OnPauseSequencePressed)
        ForceOpenButton.InteractedWithEvent.Subscribe(OnForceOpenPressed)

    OnEnablePressed(Agent : agent) : void =
        VaultDevice.Enable()
        Print("Vault device enabled!")

    OnDisablePressed(Agent : agent) : void =
        VaultDevice.Disable()
        Print("Vault device disabled!")

    OnStartSequencePressed(Agent : agent) : void =
        VaultDevice.StartSequence()
        Print("Vault sequence started by agent!")

    OnPauseSequencePressed(Agent : agent) : void =
        VaultDevice.PauseSequence()
        Print("Vault sequence paused by agent!")

    OnForceOpenPressed(Agent : agent) : void =
        VaultDevice.ForceOpen()
        Print("Vault force opened by agent!")
```

## ⚡ How to Use in UEFN
1. **Place Devices in World**
   - Add a `Bank Vault Device` from the Devices tab.
   - Place five `button_device` actors for control.

2. **Configure Vault in Details Panel**
   - Set all required gameplay options and restrictions.

3. **Create & Add Verse Script**
   - Open **Verse Explorer**.
   - Create a new `.verse` file and paste the sample code.
   - Build (Ctrl+Shift+B) until "Build Succeeded."
   - Place your Verse device and link all fields in the Details Panel.

4. **Playtest and Expand**
   - Run the game and interact with the vault.
   - Add logic for alarms, rewards, traps, or progression.

## 🧠 Best Practices
- Use `OpenEvent` to trigger in-game rewards, alarms, or mission progression.
- Combine with devices like Item Granters, Teleporters, or Spawners.
- Configure class/team access for asymmetric multiplayer gameplay.

## ❌ Common Issues & Fixes
| Problem | Likely Cause | Solution |
|--------|---------------|----------|
| Vault doesn’t open | Sequence not started or weakpoints not destroyed | Use `StartSequence()` or `ForceOpen()` |
| Damage not registering | Weakpoints not vulnerable or damage disabled | Ensure external damage enabled and wait for `WeakpointVulnerableEvent` |
| Events not firing | Device not enabled or events unsubscribed | Call `Enable()` and ensure subscriptions are present |

## ⚡ Notes
- Fully programmable stage transitions: start, pause, open, vulnerability, destruction.
- Supports PvP and PvE, and works with classic or timed game modes.
- Build complex systems using vault mechanics for immersive gameplay.

