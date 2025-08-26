# Supply Drop Spawner Device – UEFN Verse Device Documentation

## 📙 Description

The `supply_drop_spawner_device` is used to spawn and configure aerial supply drops that descend onto the island by balloon. Supply drops can contain custom loot and interact with players or teams, making them useful for battle royale, event-driven, or reward-based gameplay. Spawning, landing, and opening can be controlled through device logic in UEFN or via Verse scripting and events.

## 🧱 Verse Using Statement

```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy

- `creative_object`: Base class for creative devices and props.
- `creative_device_base`: Base class for `creative_device`.
- `supply_drop_spawner_device`

## 🧹 Data Members (Events)

| Name               | Type                | Description                                                            |
| ------------------ | ------------------- | ---------------------------------------------------------------------- |
| OpenedEvent        | listenable(agent)   | Fires when the supply crate is opened; passes the agent who opened it. |
| LandingEvent       | listenable(tuple()) | Fires when the supply crate lands on the map.                          |
| BalloonPoppedEvent | listenable(?agent)  | Fires when the balloon is popped; passes the agent or `false`.         |

## 🛠️ Functions & Methods

| Name                             | Signature / Description                                                   |
| -------------------------------- | ------------------------------------------------------------------------- |
| `Spawn()`                        | Spawns a supply drop at its spawn location.                               |
| `Spawn(agent)`                   | Spawns a supply drop with "Owning Team" set to the agent’s team.          |
| `Open(agent)`                    | Forces open the supply crate, ignoring lock status (agent as instigator). |
| `DestroyBalloon()`               | Instantly destroys the balloon, causing crate to free-fall.               |
| `Lock()`                         | Locks crate so agents cannot open it.                                     |
| `Unlock()`                       | Unlocks crate so agents may open it.                                      |
| `Enable()`                       | Enables the device.                                                       |
| `Disable()`                      | Disables the device.                                                      |
| `GetTransform()`                 | Returns device’s transform in world space (position/rotation/scale).      |
| `MoveTo(...)`, `TeleportTo(...)` | Standard `creative_object` movement methods.                              |

## 🎛 Configuration Options (Details Panel)

- **Destructible Balloon**: If true, balloon can be shot down.
- **Balloon Health**: Sets balloon HP if destructible.
- **Owning Team/Class & Invert**: Restrict/allow who can interact/damage.
- **Spawn Without Balloon**: Crate drops instantly without balloon.
- **Fall Speed**: Multiply crate descent rate.
- **Start Locked**: Starts in locked or unlocked state.
- **Spawn Radius/Location**: Island, Above, or Custom.
- **Custom Spawn Radius**: Fine-tune spread area.
- **Show Flare Where Landing**: Adds landing marker.
- **Show Icon on Minimap**: Toggle minimap indicator.
- **Spawn Delay**: Delay before initial drop spawn.
- **Custom Spawn Delay**: Manually set delay.
- **Supply FX Color, Balloon Style**: Choose VFX and balloon appearance.

## 🛠️ Example Usage in Verse

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

supply_drop_example := class(creative_device):

    @editable
    SupplyDrop : supply_drop_spawner_device = supply_drop_spawner_device{}

    @editable
    TriggerButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        SupplyDrop.OpenedEvent.Subscribe(OnDropOpened)
        SupplyDrop.LandingEvent.Subscribe(OnDropLanded)
        TriggerButton.InteractedWithEvent.Subscribe(OnButtonPressed)

    OnDropOpened(Agent : agent) : void =
        Print("Supply drop opened by player!")

    OnDropLanded() : void =
        Print("Supply drop has landed!")

    OnButtonPressed(Agent : agent) : void =
        SupplyDrop.Spawn()
        Print("Supply drop spawned!")
```

## 🧠 How It Works

1. Place a `supply_drop_spawner_device` in the UEFN editor.
2. Configure options and loot table.
3. Use a `button_device` or `.Spawn()` in Verse for triggers.
4. Subscribe to events like `OpenedEvent`, `LandingEvent`, `BalloonPoppedEvent` for custom logic.
5. Use `Lock()`, `Unlock()`, `DestroyBalloon()` for advanced interaction.

## 🧬 Best Practices

- Use `Enable()` / `Disable()` to control availability.
- Always subscribe to events for game logic.
- Configure team/class restrictions for fairness.
- Use minimap icons/flairs for player clarity.

## ❌ Incorrect Usage Examples and Fixes

| Issue                     | ❌ Wrong                  | ✅ Correct                  | Explanation                       |
| ------------------------- | ------------------------ | -------------------------- | --------------------------------- |
| Not enabling before spawn | Just call `Spawn()`      | Use `Enable()` first       | Device must be active to spawn.   |
| Not subscribing to events | Expect reward by default | Subscribe to `OpenedEvent` | Events must be handled for logic. |
| Expecting instant land    | No spawn delay set       | Set `Spawn Delay`          | Crate follows configured timing.  |
| Incorrect team settings   | All players interact     | Set `Owning Team/Class`    | Prevents unintended access.       |

## ℹ️ Notes

- Multiple drops can exist per game.
- Link events to sound/VFX for immersion.
- Use `Disable()` to despawn drops.
- Use `Lock()` / `Unlock()` for control sequencing.

