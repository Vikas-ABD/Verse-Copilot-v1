📘 Objective Device – UEFN Verse Device Documentation

🔹 Description The `objective_device` provides a collection of destructible devices you can select as objectives for your game. Players can attack or defend these devices; destroying one can award points, trigger effects, or end the match/round. It includes dynamic HUD elements, optional particle effects, explosion on destruction, a visible beacon, and options for invulnerability, health, and team assignment. You can subscribe to destruction events in Verse and control the device state, health, vulnerability, and visibility.

🛠️ Verse Using Statement

```verse
using { /Fortnite.com/Devices }
```

🔗 Inheritance Hierarchy

- creative\_object
- creative\_device\_base
- objective\_device (also implements `healthful`, `damageable`, and `healable` interfaces)

🧹 Data Members (Events)

| Name           | Type              | Description                            |
| -------------- | ----------------- | -------------------------------------- |
| DestroyedEvent | listenable(agent) | Fires when the objective is destroyed. |

🛠️ Functions & Methods

| Name                            | Description                               |
| ------------------------------- | ----------------------------------------- |
| GetHealth()                     | Gets current health value.                |
| SetHealth(float)                | Sets current health.                      |
| GetMaxHealth()                  | Gets maximum health value.                |
| SetMaxHealth(float)             | Sets max health.                          |
| Damage(float or damage\_args)   | Deals damage to the device.               |
| HealedEvent()                   | Listens for healing events.               |
| Heal(float or healing\_args)    | Heals the objective device.               |
| SetInvulnerable(logic)          | Makes the device invulnerable/damageable. |
| Show() / Hide()                 | Visually show/hide the device.            |
| Destroy(agent)                  | Immediately destroys the device.          |
| ActivateObjectivePulse(agent)   | Pulses a HUD marker for a player.         |
| DeactivateObjectivePulse(agent) | Removes the HUD pulse for a player.       |

🎛 Configuration Options (Details Panel)

| Option              | Description                                            |
| ------------------- | ------------------------------------------------------ |
| Mesh                | Destructible model to use (e.g., tower, head).         |
| Invulnerable        | Prevents damage if Yes.                                |
| Health              | Maximum hit points.                                    |
| Blast Radius        | Explosion zone size on destruction.                    |
| Beacon/Color        | Shows beacon/visual effect at location.                |
| Badge Visibility    | Controls health bar/indicator visibility.              |
| HUD Options         | HUD messages/objectives when taking damage.            |
| Owning Team         | Determines which team defends (affects HUD messaging). |
| Show/Hide on Damage | Controls indicator visibility when damaged.            |

🔍 Events

| Event                 | Trigger                                                             |
| --------------------- | ------------------------------------------------------------------- |
| DestroyedEvent(agent) | Fires when the device is eliminated, returns the responsible agent. |

🛠️ Verse Usage Example

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

objective_device_example := class(creative_device):

    @editable
    Objective : objective_device = objective_device{}

    @editable
    PulseButton : button_device = button_device{}

    @editable
    InvulnerableButton : button_device = button_device{}

    @editable
    VulnerableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        Objective.DestroyedEvent.Subscribe(OnObjectiveDestroyed)
        PulseButton.InteractedWithEvent.Subscribe(OnPulsePressed)
        InvulnerableButton.InteractedWithEvent.Subscribe(OnInvulnerablePressed)
        VulnerableButton.InteractedWithEvent.Subscribe(OnVulnerablePressed)

    OnObjectiveDestroyed(Agent : agent) : void =
        Print("Objective destroyed by agent!")

    OnPulsePressed(Agent : agent) : void =
        Objective.ActivateObjectivePulse(Agent)
        Print("Objective pulse activated for agent!")

    OnInvulnerablePressed(Agent : agent) : void =
        Objective.SetInvulnerable(true)
        Print("Objective set to invulnerable!")

    OnVulnerablePressed(Agent : agent) : void =
        Objective.SetInvulnerable(false)
        Print("Objective set to vulnerable!")
```

📖 How to Use in UEFN

1. **Place and Configure Objective Devices**

   - Drag one or more `objective_device` into the level.
   - Configure Mesh, Invulnerable, Health, Blast Radius, Ownership, HUD/Badge settings.

2. **Add Button Devices**

   - Place three `button_device` for Pulse, Invulnerable, and Vulnerable.

3. **Create Your Verse Device**

   - In Verse Explorer, create a new Verse file.
   - Paste the above code, build (Ctrl+Shift+B), and ensure build succeeds.

4. **Place and Setup Verse Device**

   - Drag the compiled Verse device into the world.
   - Set each @editable field to its corresponding device in the Details panel.

5. **Test the Setup**

   - Use Play mode.
   - Interact with buttons to see visual effects, toggle vulnerability, and observe elimination logic.

🧠 Best Practices

- Use `SetInvulnerable(true)` to gate progression (e.g., puzzle unlocks).
- Subscribe to `DestroyedEvent` for score tracking or match progression.
- Use `ActivateObjectivePulse()` to guide players using HUD.
- Show/hide/teleport the objective dynamically for evolving gameplay.

❌ Common Issues & Fixes

| Issue                    | Problem                           | Solution                                    | Explanation                         |
| ------------------------ | --------------------------------- | ------------------------------------------- | ----------------------------------- |
| Not taking damage        | Device is invulnerable            | Use `SetInvulnerable(false)`                | Enable damage for effect            |
| No elimination event     | No subscription to DestroyedEvent | Always subscribe using `.Subscribe()`       | Required for logic on destruction   |
| HUD markers unclear      | Beacon/Badge not set properly     | Configure Beacon/Badge in Details Panel     | Customizable feedback options       |
| Verse logic unresponsive | Blank references in Details panel | Set all `@editable` fields in Details panel | Required for functional Verse logic |

🔹 Use Cases:

- Attack/Defend gameplay
- Boss fights
- Stage unlocking mechanics
- Rush/detonate objectives

*This documentation serves as a full reference for implementing and using **`objective_device`** in UEFN-powered Fortnite experiences.*

