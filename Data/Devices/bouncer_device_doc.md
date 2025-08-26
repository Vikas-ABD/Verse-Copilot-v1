📘 **bouncer_device – UEFN Verse Device Documentation**

---

🔹 **Description**
The `bouncer_device` is used to create a pad or object that launches players, vehicles, and other game actors into the air with customizable velocity and optional effects (such as healing, low gravity, and enhanced air control).

**Common use cases:** bounce pads, tire stacks, mushrooms, or any interactive launcher in your Fortnite island.

🧱 **Verse Using Statement**
```verse
using { /Fortnite.com/Devices }
```

---

🔗 **Inheritance Hierarchy**
- `creative_object`
- `creative_device_base`
- `bouncer_device`

---

🧩 **Data Members (Events)**
| Name              | Type               | Description                                                                 |
|-------------------|--------------------|-----------------------------------------------------------------------------|
| BouncedEvent      | listenable(agent)  | Fires when a valid agent (usually a player) bounces—sends the agent.       |
| HealStartEvent    | listenable(agent)  | Fires when a bounce triggers a healing effect for an agent.                |
| HealStopEvent     | listenable(agent)  | Fires when a bounce healing effect ends for an agent.                      |

---

🛠️ **Functions & Methods**
| Name            | Description                                                         |
|------------------|---------------------------------------------------------------------|
| Enable()         | Enables bouncing, visuals, and audio effects.                      |
| Disable()        | Disables all bounce effects and visuals.                           |
| GetTransform()   | Returns the device’s world transform (position, rotation, scale).  |
| MoveTo(...)      | Move device to a position/rotation over time (interrupts animation).|
| TeleportTo(...)  | Instantly move to the given transform/location/rotation.           |

---

🎛 **Configuration Options (Details Panel)**
- Bounce Velocity: Set launch speed (meters/second); higher = higher/farther bounce.
- Is Indestructible: Prevents device from being damaged or destroyed.
- Device Health: Max health before device is eliminated.
- Visible During Game: Show/hide bouncer during play.
- Activating Team/Class: Restricts who can bounce.
- Forward Velocity: Add directional force; positive/negative for forward/backward.
- Bounce Direction: Bouncer orientation or vertical launch only.
- Apply Low Gravity: Adds slow-fall effect after bouncing.
- Increased Air Control: Agents can steer more easily in air.
- Heals Player: Configurable as No Heal, Instant Heal, or Periodic Heal.

---

🧰 **Verse Usage Example**
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Example device showing how to use bouncer_device
bouncer_device_example := class(creative_device):

    @editable
    Bouncer : bouncer_device = bouncer_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        # Subscribe to control buttons
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    # Button handlers
    OnEnablePressed(Agent : agent) : void =
        Bouncer.Enable()
        Print("Bouncer enabled!")

    OnDisablePressed(Agent : agent) : void =
        Bouncer.Disable()
        Print("Bouncer disabled!")
```

---

🚀 **How it works:**

1. **Place Devices in Level**:
   - Add one or more `bouncer_device` pads to your level.
   - Optionally place `button_device` objects to trigger enable/disable.

2. **Configure in Details Panel**:
   - Set Bounce Velocity, Healing, Air Control, Gravity, etc.
   - Choose Heal settings (Instant/Periodic/None).

3. **Create Verse Script**:
   - Add a new Verse file and use the example code above.
   - Build Verse code (Ctrl + Shift + B) until "Build Succeeded".

4. **Place Verse Device**:
   - Drag `bouncer_device_example` into the level.
   - Assign references in its Details panel:
     - Bouncer → your `bouncer_device`
     - EnableButton → a `button_device`
     - DisableButton → another `button_device`

5. **Test**:
   - Click *Launch Session* or *Push Changes*.
   - Interact with control buttons and test the bounce functionality.

---

🧠 **Best Practices**
- Use `.Enable()` and `.Disable()` for conditional gameplay control.
- Listen to `BouncedEvent` to trigger effects, award XP, or chain logic.
- Use team/class restrictions for advanced multiplayer logic.
- Tune Bounce Velocity and Forward Velocity for better player experience.

---

❌ **Common Mistakes & Fixes**
| Issue                    | ❌ Wrong Usage                | ✅ Correct Usage                                       | Explanation                                                   |
|--------------------------|-------------------------------|--------------------------------------------------------|---------------------------------------------------------------|
| Not enabling the device  | Bouncer won’t launch agents   | Call `.Enable()` or set enabled in Details             | Device must be enabled to activate                           |
| Expecting healing w/o config | Assume bounce will heal     | Set “Heals Player” to “Instant” or “Periodic”          | Healing only applies if enabled                              |
| Not subscribing to events| No response to bounce         | Subscribe to `BouncedEvent` in Verse                   | Enables chaining logic on bounce                             |
| Forgetting visual feedback| No launch FX/feedback        | Enable visuals, sounds, gravity effects in Details     | Improves gameplay feedback and immersion                     |

---

📌 **Notes**:
- Customize bounce and healing options for parkour, puzzles, or arena maps.
- Works with all agent types—players, vehicles, projectiles.
- Mix with VFX, triggers, and other devices for unique mechanics.

