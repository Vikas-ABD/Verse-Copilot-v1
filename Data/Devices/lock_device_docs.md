📘 lock_device – UEFN Verse Device Documentation

🔹 Description
The lock_device is used to control the locked, unlocked, open, and closed states of doors in your Fortnite island. This device only works when attached to assets that include a door (such as select galleries, props, and prefabs). You can control doors via Verse scripting, other device signals (such as from buttons, triggers, or events), or set their default state in UEFN. The device supports direct locking/unlocking, opening/closing, toggling state, and in-game access restrictions.

🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

🔗 Inheritance Hierarchy
- creative_object
- creative_device_base
- lock_device

🛠️ Functions & Methods
| Name               | Description                                     |
|--------------------|-------------------------------------------------|
| Lock(agent)        | Locks the door. Agent is the instigator.        |
| Unlock(agent)      | Unlocks the door. Agent is the instigator.      |
| ToggleLocked(agent)| Toggles between locked and unlocked.            |
| Open(agent)        | Opens the door. Agent is the instigator.        |
| Close(agent)       | Closes the door. Agent is the instigator.       |
| ToggleOpened(agent)| Toggles between open and closed.                |
| GetTransform()     | Gets current transform (position/rotation/scale)|
| MoveTo()/TeleportTo() | Move or teleport the lock/door in the world |

🎛 Configuration Options (Details Panel)
- Initial Door Position: Open/Closed at game start.
- Starts Locked: Door locked/unlocked at game start.
- Hide Interaction When Locked: Hide/fade player prompt when door is locked.
- Visible in Game: Whether device is visible during gameplay.
- Color: Color highlight for device identification.

🧹 Events
This device does not expose Verse events, but triggers, buttons, and other creative devices can drive its state through Verse or direct event binding.

🛠️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Example device showing how to use lock_device with buttons
lock_device_example := class(creative_device):

    @editable
    LockDevice : lock_device = lock_device{}

    @editable
    LockButton : button_device = button_device{}

    @editable
    UnlockButton : button_device = button_device{}

    @editable
    OpenButton : button_device = button_device{}

    @editable
    CloseButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        LockButton.InteractedWithEvent.Subscribe(OnLockPressed)
        UnlockButton.InteractedWithEvent.Subscribe(OnUnlockPressed)
        OpenButton.InteractedWithEvent.Subscribe(OnOpenPressed)
        CloseButton.InteractedWithEvent.Subscribe(OnClosePressed)

    OnLockPressed(Agent : agent) : void =
        LockDevice.Lock(Agent)
        Print("Lock engaged by agent!")

    OnUnlockPressed(Agent : agent) : void =
        LockDevice.Unlock(Agent)
        Print("Lock disengaged by agent!")

    OnOpenPressed(Agent : agent) : void =
        LockDevice.Open(Agent)
        Print("Door opened by agent!")

    OnClosePressed(Agent : agent) : void =
        LockDevice.Close(Agent)
        Print("Door closed by agent!")
```

**Explanation:**
- Reference a lock_device and up to four button_devices.
- Pressing a button triggers the corresponding action on the door.
- Extendable via triggers, overlaps, or events.

📅 How to Use in UEFN
1. **Place Door-Enabled Asset and Lock Device**
   - Add a compatible door asset.
   - Place a lock_device and attach it.

2. **Configure Door Behavior**
   - Set Initial Door Position and Starts Locked in Details panel.
   - Set Color, Hide Interaction When Locked, and visibility options.

3. **(Optional) Place Control Devices**
   - Add up to four button_devices.

4. **Create Your Verse Script**
   - In Verse Explorer, create a new Verse file.
   - Paste and save example code.
   - Build Verse Code (Ctrl+Shift+B) until "Build Succeeded" appears.

5. **Place Verse Device and Assign References**
   - Drag Verse device into level.
   - Assign LockDevice and Buttons in Details panel.

6. **Test and Iterate**
   - Use Play Mode to verify door actions.

🧠 Best Practices
- Use for puzzles, secure rooms, quests.
- Combine lock/unlock/open/close in sequence.
- Only use with compatible door assets.
- For automatic doors, use timers/events to toggle.

❌ Common Issues & Fixes
| Issue                | ❌ Error                   | ✅ Fix                          | Explanation                          |
|----------------------|------------------------------|------------------------------------|--------------------------------------|
| No effect on asset   | Used on non-door asset       | Use only with compatible door asset| Works only on door-enabled assets     |
| Events don’t fire     | No Verse/wiring trigger       | Use buttons, triggers, or Verse    | Needs trigger or Verse interaction    |
| Device reference blank| Verse reference not assigned | Set all @editable references       | Required for proper device operation |

**Note:**
- Lock and open are independent states.
- Suitable for puzzles, access controls, and events.
- All actions are runtime callable in Verse.

