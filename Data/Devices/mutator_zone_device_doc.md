## mutator\_zone\_device – UEFN Verse Device Documentation

### 🔹 Description

The `mutator_zone_device` specifies an area (zone) where a wide range of custom gameplay effects can be applied to agents inside it. Example use cases include:

- Disabling building or weapon fire
- Changing gravity
- Restricting movement
- Freezing or buffing players
- Controlling emotes/communications
- Affecting specific teams or classes

Zones can be enabled or disabled, re-targeted by team/class at runtime, and provide events for agent entry/exit and emoting.

### 🛁 Verse Using Statement

```verse
using { /Fortnite.com/Devices }
```

### 🔗 Inheritance Hierarchy

- `creative_object`
- `creative_device_base`
- `effect_volume_device`
- `mutator_zone_device`

### 🧩 Data Members (Events)

| Name                    | Type              | Description                                         |
| ----------------------- | ----------------- | --------------------------------------------------- |
| AgentEntersEvent        | listenable(agent) | Fires when an agent enters the mutator zone.        |
| AgentExitsEvent         | listenable(agent) | Fires when an agent leaves the mutator zone.        |
| AgentBeginsEmotingEvent | listenable(agent) | Fires when an agent starts emoting inside the zone. |
| AgentEndsEmotingEvent   | listenable(agent) | Fires when an agent stops emoting inside the zone.  |

### 🛠️ Functions & Methods

| Name                       | Description                                                       |
| -------------------------- | ----------------------------------------------------------------- |
| Enable()                   | Enables the zone (activates its gameplay effects).                |
| Disable()                  | Disables the zone (removes all zone effects).                     |
| UpdateSelectedTeam(agent)  | Future effects will target agent’s team.                          |
| UpdateSelectedClass(agent) | Future effects will target agent’s class.                         |
| IsInVolume(agent)          | Succeeds if an agent is in this zone (usable in failure context). |
| GetAgentsInVolume()        | Returns array of agents currently inside the zone.                |
| MoveTo() / TeleportTo()    | Move/teleport the zone device.                                    |
| GetTransform()             | Returns world position/rotation/scale of the device.              |

### 🎮 Configuration Options (Details Panel)

- **Enabled on Phase**: When this device is active (All, Pre-Game, Gameplay).
- **Zone Visible During Game**: Display/hide zone FX in gameplay.
- **Zone Base Visible**: Show/hide base mesh.
- **Zone Shape (Box/Cylinder)**: Physical shape of the area.
- **Width/Depth/Height**: Physical size of the zone.
- **Selected Team/Class**: Which team/class the zone affects.
- **Invert Class/Team Selection**: Restrict/allow by exclusion.
- **Affects Players/Creatures/Guards**: Select who is affected.
- **Allow Weapon Fire/Building/Editing/Jumping**: Grant or remove basic gameplay abilities.
- **Gravity Override**: Set custom gravity for agents in the zone.
- **Movement Multiplier**: Adjust movement speed or freeze players.
- **Pickup Life Span**: Destroy items after set time when dropped in zone.
- **Enable VFX**: Play visual effects when a player crosses the zone.
- **Allow Emote Wheel/Map Marker**: Control communication and ping ability inside zone.

### 🛠️ Verse Usage Example

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

mutator_zone_example := class(creative_device):

    @editable
    MutatorZone : mutator_zone_device = mutator_zone_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    UpdateTeamButton : button_device = button_device{}

    @editable
    UpdateClassButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        MutatorZone.AgentEntersEvent.Subscribe(OnAgentEnters)
        MutatorZone.AgentExitsEvent.Subscribe(OnAgentExits)
        MutatorZone.AgentBeginsEmotingEvent.Subscribe(OnAgentBeginsEmoting)
        MutatorZone.AgentEndsEmotingEvent.Subscribe(OnAgentEndsEmoting)

        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        UpdateTeamButton.InteractedWithEvent.Subscribe(OnUpdateTeamPressed)
        UpdateClassButton.InteractedWithEvent.Subscribe(OnUpdateClassPressed)

    OnAgentEnters(Agent : agent) : void =
        Print("Agent entered the mutator zone!")

    OnAgentExits(Agent : agent) : void =
        Print("Agent exited the mutator zone!")

    OnAgentBeginsEmoting(Agent : agent) : void =
        Print("Agent began emoting in the mutator zone!")

    OnAgentEndsEmoting(Agent : agent) : void =
        Print("Agent ended emoting in the mutator zone!")

    OnEnablePressed(Agent : agent) : void =
        MutatorZone.Enable()
        Print("Mutator zone enabled!")

    OnDisablePressed(Agent : agent) : void =
        MutatorZone.Disable()
        Print("Mutator zone disabled!")

    OnUpdateTeamPressed(Agent : agent) : void =
        MutatorZone.UpdateSelectedTeam(Agent)
        Print("Mutator zone team updated!")

    OnUpdateClassPressed(Agent : agent) : void =
        MutatorZone.UpdateSelectedClass(Agent)
        Print("Mutator zone class updated!")
```

### 🔍 How it Works in UEFN

1. **Place Devices in Level**:
   - Add `mutator_zone_device` where you want gameplay logic to apply.
   - Add `button_device` for in-game controls.
2. **Configure Device in Details Panel**:
   - Set shape, size, phase, effects, team/class filters.
3. **Create & Build Verse Script**:
   - Create file in Verse Explorer, paste script, and build.
4. **Place and Reference Verse Device**:
   - Add your `mutator_zone_example` to the map.
   - Assign references to your actual devices in Details panel.
5. **Test In-Game**:
   - Walk through the zone, test buttons, and observe log output.

### 🧠 Best Practices

- Use multiple zones for layered effects.
- Dynamically update targets via `UpdateSelectedTeam` / `UpdateSelectedClass`.
- Use events for scoring, UI updates, or triggers.
- Combine with timer/trigger devices for puzzles and round logic.

### ❌ Incorrect Usage Examples

| Issue                     | ❌ Wrong Example                          | ✅ Correct Example                                       | Explanation                                 |
| ------------------------- | ---------------------------------------- | ------------------------------------------------------- | ------------------------------------------- |
| Not subscribing to events | `MutatorZone.AgentEntersEvent`           | `MutatorZone.AgentEntersEvent.Subscribe(OnAgentEnters)` | Must use `.Subscribe()` for event handling. |
| Assuming zone affects all | Didn't configure team/class              | Configure `team/class/creature/guard` in Details        | Must define affected groups.                |
| Missing device references | Left `MutatorZone` or buttons unassigned | Assign in Details panel                                 | Required for functioning script.            |
| Wrong device method call  | `SomeOtherDevice.Enable()`               | `MutatorZone.Enable()`                                  | Use correct device instance.                |
| Using disabled zone       | Zone placed but not enabled              | Use `Enable()` in Verse or enable in Details            | Must be active to apply effects.            |

### ⚠️ Notes

- Effects/affinity must be configured in the Details panel or through runtime methods.
- Use subscriptions to add reactive behavior to gameplay.
- Perfect for dynamic maps, custom game modes, and creative challenges.

