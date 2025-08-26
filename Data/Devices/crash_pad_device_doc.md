📘 crash_pad_device – UEFN Verse Device Documentation

🔹 Description
The crash_pad_device is used to place a Crash Pad in your Fortnite island that launches players (and certain objects) upward, protecting them from fall damage. Crash Pads can be customized for visual style, activation phase, and launch event handling. These are ideal for puzzles, obstacle courses, movement challenges, or any scenario where you want to boost players and prevent fall eliminations.

🧱 Verse Using Statement
verse
using { /Fortnite.com/Devices }

🔗 Inheritance Hierarchy
* creative_object
* creative_device_base
* crash_pad_device

🧩 Data Members (Events)
| Name           | Type             | Description                                      |
|----------------|------------------|--------------------------------------------------|
| LaunchedEvent | listenable(agent) | Fires when an agent (player, vehicle, etc.) is launched by this pad. |

🛠️ Functions & Methods
| Name         | Description                                                  |
|--------------|--------------------------------------------------------------|
| Enable()     | Enables the crash pad for launch/bounce.                    |
| Disable()    | Disables the device, deactivating launch and visuals.       |
| GetTransform() | Returns the world transform (position/rotation/scale).     |
| MoveTo(...)  | Moves device to a specified transform over time.            |
| TeleportTo(...) | Instantly move device to position/rotation/transform.     |

🎛 Configuration Options (Details Panel)
| Option                          | Description                                                   |
|--------------------------------|---------------------------------------------------------------|
| Device Health                  | Indestructible or custom number; controls damage before pad breaks. |
| Enabled During Phase           | Always, Pre-Game, Gameplay Only, Create Only, None.           |
| Visual Style                   | Default, Original, Target.                                    |
| Allow Any Launch to Send Event | On/Off—event for any bounce, not just players/vehicles.       |

🧰 Usage Example in Verse
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

crash_pad_example := class(creative_device):

    @editable
    CrashPad : crash_pad_device = crash_pad_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        # Subscribe to crash pad launch events
        CrashPad.LaunchedEvent.Subscribe(OnPlayerLaunched)

        # Subscribe to control buttons
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    # Event handler for player launch
    OnPlayerLaunched(Agent : agent) : void =
        Print("Player was launched by crash pad!")

    # Button handlers
    OnEnablePressed(Agent : agent) : void =
        CrashPad.Enable()
        Print("Crash pad enabled!")

    OnDisablePressed(Agent : agent) : void =
        CrashPad.Disable()
        Print("Crash pad disabled!")
```

📋 How it works:
* **Place Devices in Level:**
  * Add a crash_pad_device to your level.
  * (Optional) Add button_devices and assign them as Enable or Disable controls.
* **Configure in Details Panel:**
  * Set device health, enabled phase, visual style, and event options as needed.
* **Create the Verse Script:**
  * Add a new Verse script (crash_pad_example.verse), paste the code above, and save.
  * Build the Verse code (Verse → Build Verse Code or CTRL+SHIFT+B).
* **Place Verse Device:**
  * Drag crash_pad_example from the Content Browser into your level.
  * In its Details panel, assign:
    * CrashPad → your crash_pad_device
    * EnableButton → a button_device to enable the pad
    * DisableButton → a button_device to disable the pad
* **Test:**
  * Launch a session. See log output when a player is launched, and use the buttons to enable/disable the pad.

🧠 Best Practices
* Use .Enable() and .Disable() in Verse or via button triggers to control the pad during rounds, puzzles, or events.
* Subscribe to LaunchedEvent to run custom logic, such as playing effects, granting XP, or unlocking progress.
* Place pads in areas where falls occur to eliminate fall damage risks.
* Consider disabling during certain phases to restrict pad use.
* Set “Allow Any Launch to Send Event” to On for more advanced logic with props or vehicles.

❌ Common Mistakes & Fixes
| Issue                     | ❌ Wrong Usage             | ✅ Correct Usage                  | Explanation                              |
|--------------------------|----------------------------|----------------------------------|------------------------------------------|
| Not enabling pad         | Pad does nothing           | Call .Enable() or set enabled phase | Must be enabled to launch agents         |
| Not subscribing to event | No bounce logic or VFX     | Subscribe in Verse as shown above | Unlocks custom logic when bounce occurs |
| Conflicting device config| Set pad disabled/destructible | Adjust health & phase             | Pad can be persistent or destructible   |
| Expecting healing/slow fall | Use wrong device         | Use crash_pad to bounce only       | Pad only protects from fall eliminations |

📌 Note:
* For generalized directional or configurable velocity launches, use `bouncer_device`.
* For minigame or progression logic, tie the crash_pad_device to event chains or logic via Verse.
* Combine with other creative devices for multi-stage obstacles, parkour, or secret areas.

