📘 **player_checkpoint_device – UEFN Verse Device Documentation**

🔹 **Description**
The `player_checkpoint_device` sets an agent’s (player’s) current respawn (spawn) point when activated. It can also clear the agent’s inventory, depending on device options. Use checkpoints for progression, respawn management, or to mark level segments. Agents can activate a checkpoint by interacting with it or by using Verse to register them directly.

🧱 **Verse Using Statement**
```verse
using { /Fortnite.com/Devices }
```

🔗 **Inheritance Hierarchy**
- `creative_object`: Base class for creative devices and props.
- `creative_device_base`: Base class for `creative_device`.
- `player_checkpoint_device`

🧩 **Data Members (Events)**
| Name                         | Type                | Description                                                        |
|------------------------------|---------------------|--------------------------------------------------------------------|
| `FirstActivationEvent`       | `listenable(agent)` | Fires when the device is activated for the first time by any agent.|
| `FirstActivationPerAgentEvent` | `listenable(agent)` | Fires the first time a specific agent activates this checkpoint.    |

🛠️ **Functions & Methods**
| Name                 | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| `Register(agent)`    | Registers the agent. Sets their respawn point to this device—may clear inventory.|
| `Enable()`           | Enables the checkpoint (activate via triggers, events, or Verse).           |
| `Disable()`          | Disables the device; agents can’t register or trigger it until re-enabled. |
| `GetRegisteredAgents()` | Returns array of agents currently registered to this checkpoint.        |
| `IsRegistered(agent)`| Returns true if this agent is registered at this checkpoint.               |
| `GetTransform()`     | Returns checkpoint’s transform (location, rotation, scale in cm).         |
| `MoveTo(...) / TeleportTo(...)` | Standard creative_object movement.                           |

🎛 **Configuration Options (Details Panel)**
- **Visible in Game**: On/Off — affects visibility and agent collision.
- **Reset Inventory**: Yes/No — clears inventory when checkpoint registered.
- **Enabled During Phase**: None / All / Create Only / Game Countdown Only / Gameplay Only
- **Activating Team**: Any or restrict to a specific team.
- **Play Activate FX**: On/Off — visual/sound effects when activated.
- **Allowed Class**: Any, No Class, or restrict to class.

🧰 **Example Usage in Verse**
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

player_checkpoint_example := class(creative_device):

    @editable
    PlayerCheckpoint : player_checkpoint_device = player_checkpoint_device{}

    @editable
    RegisterButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        PlayerCheckpoint.FirstActivationEvent.Subscribe(OnFirstActivation)
        PlayerCheckpoint.FirstActivationPerAgentEvent.Subscribe(OnFirstActivationPerAgent)
        RegisterButton.InteractedWithEvent.Subscribe(OnRegisterPressed)

    OnFirstActivation(Agent : agent) : void =
        Print("Checkpoint activated for the first time!")

    OnFirstActivationPerAgent(Agent : agent) : void =
        Print("Checkpoint activated for this agent for the first time!")

    OnRegisterPressed(Agent : agent) : void =
        PlayerCheckpoint.Register(Agent)
        Print("Checkpoint registered and inventory cleared for agent!")
```

**How it works:**
- Place one or more `player_checkpoint_device` in your level.
- Configure options in the Details panel: visibility, clearing inventory, permitted teams, classes, and activation FX.
- Use Verse to subscribe to activation events for progression, reward, visual feedback, or chained logic:
  - `FirstActivationEvent` triggers the first time *any* player activates the checkpoint.
  - `FirstActivationPerAgentEvent` triggers the first time *each player* activates it.
- In Verse, call `.Register(Agent)` to set a player’s current checkpoint and clear their inventory (if desired).
- Use triggers, buttons, or custom logic to register agents to checkpoints (via direct interaction, volume triggers, or event chains).

🧠 **Best Practices**
- Place a checkpoint at any advancement, save, or respawn milestone in your experience.
- Use `.Register()` in Verse to set the checkpoint based on custom triggers (like button press, puzzle completion).
- Toggle “Reset Inventory” as needed: On for challenge/puzzle games, Off for linear progression or story modes.
- Use event subscriptions to unlock content, trigger sounds/VFX, or show notifications on activation—rewarding player progression.
- Combine with `player_spawner_device` for reliable, feature-rich spawn/respawn control.

❌ **Incorrect Usage Examples and How to Fix**
| Issue                               | ❌ Wrong                             | ✅ Correct                                      | Explanation                                                   |
|-------------------------------------|--------------------------------------|------------------------------------------------|---------------------------------------------------------------|
| Only placing device, no event logic | No feedback or logic on activation  | Subscribe to activation events in Verse        | Unlocks custom progression & gameplay feedback               |
| Registering agent with device disabled | Call `.Register()` when disabled   | Always ensure checkpoint is enabled            | Only enabled checkpoints can register agents                 |
| Expecting inventory always clears   | Forgetting to set “Reset Inventory” | Set “Reset Inventory” to Yes, as needed        | Must enable to clear inventory automatically                 |
| Not configuring allowed team/class  | All agents allowed by default       | Use team/class filters for stricter progression | Prevents wrong players activating/saving checkpoint          |

**Note:**
- Useful for campaign progression, multiplayer checkpoints, and advanced respawn systems.
- Inventory clear can be used for “clean slates” at challenges or gauntlets.
- Use `FirstActivation` events for special logic (unlocking doors, VFX, sound cues, etc.).

