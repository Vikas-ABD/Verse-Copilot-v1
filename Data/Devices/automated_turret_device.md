# automated\_turret\_device – UEFN Verse Device Documentation

## 🔹 Description

The `automated_turret_device` in Unreal Editor for Fortnite (UEFN) is a gameplay device that functions as a customizable automated turret. It can scan for nearby targets within a configurable area, rotate to aim, and automatically attack players or AI that meet the filtering criteria. You can dynamically enable, disable, or retarget the turret in Verse, making it suitable for tower defense, area denial, base protection, and PvE/PvP scenarios.

## 🧱 Imports Required

```verse
verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy

- `creative_object`
- `creative_device_base`
- `automated_turret_device` (also implements `healthful` and `healable`)

## 🧹 Core Methods

| Function Signature                                         | Description                                                                       |
| ---------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `Enable(): void`                                           | Enables the turret to scan, rotate, and track targets.                            |
| `Disable(): void`                                          | Disables the turret; it closes and ignores its activation radius.                 |
| `SetDamage(Damage: float): void`                           | Sets how much damage the turret does per shot.                                    |
| `SetActivationRange(Range: float): void`                   | Sets in meters the distance at which the turret activates (clamped 2–100 meters). |
| `SetTargetRange(Range: float): void`                       | Sets the targeting range in meters (clamped 2–100; <2 disables targeting).        |
| `SetTarget(Agent: agent): void`                            | Makes the turret attempt to target a specific agent if in range/LOS.              |
| `ClearTarget(): void`                                      | Clears the current target; turret resumes scanning.                               |
| `GetTarget(): ?agent`                                      | Returns the current agent targeted by this device, if any.                        |
| `SetTeam(Agent: agent): void`                              | Sets the turret’s team to match the provided agent (restrictions apply).          |
| `UseDefaultTeam(): void`                                   | Assigns the turret to the default team (restrictions apply).                      |
| `UseTeamWildlifeAndCreatures(): void`                      | Assigns the turret to the Wildlife & Creatures team (restrictions apply).         |
| `GetHealth(), SetHealth(), GetMaxHealth(), SetMaxHealth()` | Healthful and healable interface operations.                                      |
| `Heal(Amount: float)` / `Heal(Args: healing_args)`         | Fully or partially heal the turret; triggers `HealedEvent`.                       |

## 📡 Key Events

| Event Name         | Description                                                                        |
| ------------------ | ---------------------------------------------------------------------------------- |
| `ActivatedEvent`   | Fires when an agent enters the activation radius (sends optional agent).           |
| `DamagedEvent`     | Fires when the turret is damaged (sends optional agent who caused damage).         |
| `DestroyedEvent`   | Fires when turret is destroyed (sends optional agent responsible).                 |
| `TargetFoundEvent` | Fires when a valid target is detected in range; sends the agent found.             |
| `TargetLostEvent`  | Fires when the current target is lost (e.g., moves out of range or line-of-sight). |
| `HealedEvent`      | Fires when the turret is healed (provides healing result payload).                 |

## 📰 Configuration Options (Details Panel)

- **Possible Targets:** Everyone / Neutral or Hostile / Hostile Only
- **Starting Team Type:** Team Index / Wildlife and Creatures
- **Default Team:** If Team Index chosen
- **Can Target Players:** True / False
- **Activation Radius / Max Target Distance**
- **Start Enabled:** True / False
- **Device Health / Destruction Behavior / Respawn**
- **Go Dormant if Alone:** True / False
- **Visual Options:** Wire display, color, etc.

## 🛠️ Usage Example

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }

# Device to manage automated turret behavior
turret_manager := class(creative_device):

    @editable
    Turret : automated_turret_device = automated_turret_device{}
    @editable
    EnableButton : button_device = button_device{}
    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        # Subscribe to turret events
        Turret.TargetFoundEvent.Subscribe(OnTargetFound)
        Turret.TargetLostEvent.Subscribe(OnTargetLost)
        Turret.DamagedEvent.Subscribe(OnTurretDamaged)
        Turret.DestroyedEvent.Subscribe(OnTurretDestroyed)

        # Bind button interactions
        EnableButton.InteractedWithEvent.Subscribe(OnEnableTurret)
        DisableButton.InteractedWithEvent.Subscribe(OnDisableTurret)

    OnTargetFound(Agent : agent) : void =
        Print("Turret found a target!")

    OnTargetLost(Agent : agent) : void =
        Print("Turret lost its target!")

    OnTurretDamaged(MaybeAgent : ?agent) : void =
        Print("Turret was damaged!")

    OnTurretDestroyed(MaybeAgent : ?agent) : void =
        Print("Turret was destroyed!")

    OnEnableTurret(Agent : agent) : void =
        Turret.Enable()

    OnDisableTurret(Agent : agent) : void =
        Turret.Disable()
```

## 🧠 Best Practices

- Place and configure your `automated_turret_device` in UEFN, specifying team, range, damage, and possible targets.
- Use Verse to dynamically enable, disable, or retarget the turret during gameplay.
- Subscribe to events for logic like alarms, effects, or respawn behavior.
- Check "Possible Targets" setting before using team/target functions.
- Combine with triggers, buttons, or timers for advanced logic.

## ❌ Incorrect Usage Examples and Fixes

| Issue                               | ❌ Wrong Example                                                  | ✅ Correct Example                               | Explanation                                      |
| ----------------------------------- | ---------------------------------------------------------------- | ----------------------------------------------- | ------------------------------------------------ |
| Not assigning device ref            | Calling turret method without `@editable` or Details panel setup | Assign in Details and mark field `@editable`    | Device reference must be initialized and exposed |
| Setting range out of bounds         | `SetActivationRange(150.0)`                                      | `SetActivationRange(Min(100.0, DesiredRange))`  | Range must be between 2–100 meters               |
| Forcing target outside range        | Targeting agent not in range or team                             | Ensure agent is within radius and on valid team | Targeting only works if valid                    |
| Ignoring "Possible Targets" setting | Changing team when set to "Everyone"                             | Use team/target functions only when appropriate | APIs behave differently based on target config   |

## Notes

- Mesh, animations, damage, and behavior are set in the device’s Details panel.
- Target/team assignment APIs only work as expected if "Possible Targets" ≠ Everyone.
- Always use `@editable` to expose turret and button references.
- Events and Verse provide full control for dynamic combat scenarios.

