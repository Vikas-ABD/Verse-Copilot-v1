📘 **prop_mover_device – UEFN Verse Device Documentation**

---

### 🔹 Description
The `prop_mover_device` is used to move props, building pieces, or other devices within your Fortnite island—allowing for dynamic platforms, traps, and interactive elements. The device enables you to control movement (start, stop, reverse, reset, set speed/distance), as well as respond to collisions with agents, AI, or other props. It's essential for moving platforms, puzzles, dynamic traps, and advanced game flow using Verse and device binding.

---

### 🧱 Imports Required
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
```

---

### 🔗 Inheritance Hierarchy
- `creative_object`
  *Base class for creative devices and props.*
- `creative_device_base`
  *Base class for creative_device.*
- `prop_mover_device`

---

### 🧩 Core Methods & Events
| Name / Function | Type / Signature | Description |
|-----------------|------------------|-------------|
| `Enable()` | `void` | Enables the device for movement and events. |
| `Disable()` | `void` | Disables the device (stops prop control). |
| `Begin()` | `void` | Begins moving the prop along the configured path. |
| `End()` | `void` | Stops moving the prop. |
| `Advance()` | `void` | Moves the prop forward, ignoring previous movement. |
| `Reverse()` | `void` | Reverses the prop's movement direction. |
| `Reset()` | `void` | Returns the prop to its initial position. |
| `SetTargetDistance(float)` | `void` | Sets total distance (meters) for the prop movement. |
| `GetTargetDistance()` | `float` | Gets configured movement distance (meters). |
| `SetTargetSpeed(float)` | `void` | Sets speed (meters/second) for prop movement. |
| `GetTargetSpeed()` | `float` | Gets current movement speed. |
| `BeganEvent` | `listenable(tuple())` | Fires when prop movement begins. |
| `EndedEvent` | `listenable(tuple())` | Fires when prop movement ends. |
| `FinishedEvent` | `listenable(tuple())` | Fires when prop reaches destination. |
| `AgentHitEvent` | `listenable(agent)` | Fires and passes agent when the moving prop collides with a player. |
| `AIHitEvent` | `listenable(tuple())` | Fires when the prop collides with AI, creature, or NPC. |
| `PropHitEvent` | `listenable(tuple())` | Fires when the moving prop collides with another prop. |

---

### 🎛 Configuration Options (Details Panel)
| Option | Values/Description |
|--------|---------------------|
| Distance Measurement | Metric, Tile |
| Distance | Meters or Tiles (total move distance) |
| Speed | Meters/sec or Tiles/sec |
| On Player Collision | Continue, Stop, Reverse, Push, plus Damage |
| On Prop Collision | Continue, Stop, Reverse, plus Damage |
| On AI Collision | Continue, Stop, Reverse, Push, plus Damage |
| Path Complete Action | None, Ping Pong, Repeat, Reset |

*Set all device options in Details panel in UEFN*

---

### 🧰 Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

prop_mover_example := class(creative_device):

    @editable
    PropMover : prop_mover_device = prop_mover_device{}

    @editable
    StartButton : button_device = button_device{}

    @editable
    StopButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        # Link button/device actions
        StartButton.InteractedWithEvent.Subscribe(OnStart)
        StopButton.InteractedWithEvent.Subscribe(OnStop)

        # Set movement parameters
        PropMover.SetTargetDistance(10.0) # meters
        PropMover.SetTargetSpeed(5.0) # meters/sec

        # Subscribe to collision/movement events
        PropMover.AgentHitEvent.Subscribe(OnAgentHit)
        PropMover.PropHitEvent.Subscribe(OnPropHit)
        PropMover.BeganEvent.Subscribe(OnMoveBegin)
        PropMover.FinishedEvent.Subscribe(OnMoveFinished)

    OnStart(Agent : agent) : void =
        Print("Prop started moving!")
        PropMover.Begin()

    OnStop(Agent : agent) : void =
        Print("Prop stopped moving!")
        PropMover.End()

    OnAgentHit(HitAgent : agent) : void =
        Print("Moving prop collided with a player/agent!")

    OnPropHit(params : tuple()) : void =
        Print("Moving prop collided with another prop!")

    OnMoveBegin(params : tuple()) : void =
        Print("Prop movement began.")

    OnMoveFinished(params : tuple()) : void =
        Print("Prop reached its destination.")
```

---

### 🧠 Best Practices
- Set collision behaviors and damage in Details to match your gameplay (e.g., “Reverse” for trap, “Push” for elevator).
- Start with props hidden or disabled as needed for puzzle/trigger platforms.
- Use Verse event subscriptions to link movement to triggers, deadlines, or player interaction.
- Use `Reset()` to return prop to original location before a round or between attempts.

---

### ❌ Common Mistakes & Fixes
| Issue | ❌ Wrong Example | ✅ Correct Example | Explanation |
|-------|------------------|--------------------|-------------|
| Not assigning device ref | Ref in code but not linked in panel | Always link via `@editable` & assign in Details | Prevents null/error calls in Verse |
| Not setting movement config | Skipping Distance/Speed | Set in Details or with `SetTargetDistance/Speed()` | Prop won’t move as intended |
| Ignoring collision events | Not subscribing to event | Always use `.Subscribe()` in Verse or via device | Misses important gameplay moments |

---

### Note:
- Path, speed, collision, and advanced event settings are edited per-instance in UEFN; override or re-configure in Verse as appropriate.
- For full animation or sequence control, combine with triggers, timers, and/or external logic devices.
- Prop mover works on building pieces, devices, large props—make sure device sphere “attaches” in editor for correct movement.

