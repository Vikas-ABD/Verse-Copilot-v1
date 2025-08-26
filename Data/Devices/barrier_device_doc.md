📘 **barrier_device – UEFN Verse Device Documentation**

🔹 **Description**
The `barrier_device` creates an impenetrable zone that blocks both agent movement and weapon fire. It is useful for setting up map borders, restricted areas, spawn zones, or interactive barriers that can be enabled/disabled during gameplay. Additional features include ignoring specific agents, teams, or classes and customizing visual style, shape, and collision.

🧱 **Verse Using Statement**
```verse
using { /Fortnite.com/Devices }
```

🔗 **Inheritance Hierarchy**
- creative_object
- creative_device_base
- barrier_device

🧩 **Functions & Methods**
| Name | Description |
|------|-------------|
| Enable() | Enables the barrier (activates collision/visuals as set). |
| Disable() | Disables the barrier (removes collision/can become invisible). |
| AddToIgnoreList(agent) | Allows a specific agent to pass through this barrier. |
| RemoveFromIgnoreList(agent) | Removes an agent from ignore list; they’re blocked again unless ignored via team/class. |
| RemoveAllFromIgnoreList() | Clears ignore list for all agents; team/class ignore may still apply. |
| GetTransform() | World position/rotation/scale of the barrier. |
| MoveTo(...)/TeleportTo(...) | Move/teleport barrier device. |

🧩 **Events**
- No direct gameplay events; state is driven by Verse/script/wires.

🎛 **Configuration Options (Details Panel)**
- **Enabled During Phase**: None, Always, Pre-Game, Gameplay – auto-activation rules.
- **Visible During Game**: Show/hide barrier visuals.
- **Barrier Material**: Style (including invisible, forcefield, colors).
- **Zone Shape**: Box, Hollow Box, Cylinder, etc.
- **Width/Depth/Height**: Set size in Creative tiles/meters.
- **Block Weapon Fire**: If on, also blocks bullets/projectiles.
- **Collide With Camera**: If enabled, blocks player’s camera.
- **Ignore Team/Class**: Allows members of a team/class to pass through.
- **Shrink to Allow Building**: Shrinks slightly for build placement near/inside.
- **Invisible to Ignored Players**: Makes barrier unseen/collision-less to agents on ignore list.

🧰 **Verse Usage Example**
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

barrier_device_example := class(creative_device):

    @editable
    Barrier : barrier_device = barrier_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    IgnoreButton : button_device = button_device{}

    @editable
    UnignoreButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        IgnoreButton.InteractedWithEvent.Subscribe(OnIgnorePressed)
        UnignoreButton.InteractedWithEvent.Subscribe(OnUnignorePressed)

    OnEnablePressed(Agent : agent) : void =
        Barrier.Enable()
        Print("Barrier enabled!")

    OnDisablePressed(Agent : agent) : void =
        Barrier.Disable()
        Print("Barrier disabled!")

    OnIgnorePressed(Agent : agent) : void =
        Barrier.AddToIgnoreList(Agent)
        Print("Agent added to barrier ignore list!")

    OnUnignorePressed(Agent : agent) : void =
        Barrier.RemoveFromIgnoreList(Agent)
        Print("Agent removed from barrier ignore list!")
```

🧪 **How it Works in UEFN**
1. **Place Devices in Level**
   - Add a `barrier_device` to block movement/fire.
   - Add `button_device` nearby for toggling functions.
2. **Configure in Details Panel**
   - Adjust shape, size, visual/collision properties, and ignore rules.
3. **Create & Build Verse Script**
   - Paste code into a new file (e.g., `barrier_device_example.verse`), save and build (Ctrl+Shift+B).
4. **Place Verse Device**
   - Drag `barrier_device_example` onto map.
   - Assign `Barrier`, `EnableButton`, `DisableButton`, `IgnoreButton`, and `UnignoreButton` in Details panel.
5. **Test In-Game**
   - Test barrier collision, weapon blocking, and button interactions.

🧠 **Best Practices**
- Ideal for base defense, spawn rooms, or unlockable paths.
- Use ignore lists for stealth passages or dynamic access.
- Invisible material = hidden walls.
- Combine with teams/classes for complex team-based rules.

❌ **Incorrect Usage Examples and Fixes**
| Issue | ❌ Wrong Example | ✅ Correct Example | Explanation |
|-------|------------------|-------------------|-------------|
| Not checking if agent is in ignore list | Barrier.AddToIgnoreList(SomeAgent) (any context) | Barrier.AddToIgnoreList(SomeAgent) | No check needed – call directly. |
| Confusing team/class ignore vs. list | Only use team ignore | Use both team/class config + AddToIgnoreList | All ignore methods stack additively. |
| Expecting weapon fire to be blocked | Barrier enabled but not blocking bullets | Set "Block Weapon Fire" = On in Details | Must enable in Details. |
| Trying to toggle via Details | Change Enable state from Details | Use Barrier.Enable()/Disable() in Verse | Must use code for runtime control. |
| Unassigned Verse device references | Didn’t assign Barrier/Buttons | Assign all in Details panel | Required for Verse to work. |

📌 **Note**:
- Runtime Verse or wire control required for dynamic use.
- Team/class/agent ignore layers stack for flexible gameplay.
- Use overlapping barriers for advanced control.

