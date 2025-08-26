📘 **ai_patrol_path_device – UEFN Verse Device Documentation**

🔹 **Description**
The `ai_patrol_path_device` is used to define patrol routes for guards spawned from a `guard_spawner_device`. You configure the patrol path in the editor by adding patrol nodes, setting direction/order, and choosing patrolling behavior (loop, back and forth, stop at end). This device lets you build complex or simple patrol networks for AI guards, supporting advanced gameplay such as stealth, base defense, or interactive objectives.

🧱 **Verse Using Statement**
```verse
using { /Fortnite.com/Devices }
```

🔗 **Inheritance Hierarchy**
- creative_object
- creative_device_base
- ai_patrol_path_device

🧩 **Data Members (Events)**
| Event Name               | Type                   | Description                                     |
|--------------------------|------------------------|-------------------------------------------------|
| NodeReachedEvent         | listenable(payload)    | Fires when a guard reaches this path node.      |
| NextNodeUnreachableEvent | listenable(payload)    | Fires if a guard cannot reach the next node.    |
| PatrolPathStartedEvent   | listenable(payload)    | Fires when a guard starts on this patrol path.  |
| PatrolPathStoppedEvent   | listenable(payload)    | Fires when a guard stops using this patrol path.|

🛠️ **Functions & Methods**
| Name                    | Description                                                 |
|-------------------------|-------------------------------------------------------------|
| Assign(Agent: agent)    | Assign a specific AI to this patrol path.                   |
| Enable()                | Enables the patrol path device.                             |
| Disable()               | Disables the patrol path device. Guards stop patrolling.    |
| GoToNextPatrolGroup()   | Command patrollers to follow the configured next group.     |
| GetTransform()          | Returns the device’s position/rotation/scale.               |
| MoveTo(...)/TeleportTo(...) | Move/teleport device to new transform.                  |

🎛 **Configuration Options (Details Panel)**
| Option                    | Description                                                         |
|---------------------------|---------------------------------------------------------------------|
| Patrol Path Group         | Assign a group for routing/switching complex patrol networks.       |
| Next Patrol Path Group    | Set the group to switch to via Verse or event-driven methods.       |
| Patrol Path Ordering      | Determines order within the group.                                 |
| Enabled at Start          | Should path be active when round starts.                           |
| Patrolling Mode           | Back & Forth, Looping, Stop at End.                                |
| Show Path in Play/Edit    | Toggle path debug visualizations.                                  |

🧰 **Verse Usage Example**
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

patrol_path_example := class(creative_device):

    @editable
    PatrolPath : ai_patrol_path_device = ai_patrol_path_device{}

    @editable
    GuardSpawner : guard_spawner_device = guard_spawner_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        GuardSpawner.SpawnedEvent.Subscribe(OnGuardSpawned)
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    OnGuardSpawned(Agent : agent) : void =
        Print("Guard spawned and assigned to patrol path!")
        PatrolPath.Assign(Agent)

    OnEnablePressed(Agent : agent) : void =
        PatrolPath.Enable()
        Print("Patrol path enabled!")

    OnDisablePressed(Agent : agent) : void =
        PatrolPath.Disable()
        Print("Patrol path disabled!")
```

🔄 **How it works in UEFN:**
1. **Place Devices in Level:**
    - Add one or more `ai_patrol_path_device` nodes.
    - Add a `guard_spawner_device` to spawn guards.
    - (Optional) Add `button_devices` for path control.
2. **Configure Devices:**
    - Add nodes to path and configure behavior/group in Details panel.
    - Assign the patrol path to the `guard_spawner_device`.
3. **Create and Build Verse Script:**
    - Create a new file in Verse Explorer.
    - Paste and save the example code.
    - Build Verse code (CTRL+SHIFT+B).
4. **Place & Connect Devices:**
    - Drag Verse device into map.
    - Assign PatrolPath, GuardSpawner, and buttons in Details panel.
5. **Test the Behavior:**
    - Launch session.
    - Guards follow the path.
    - Toggle path with buttons.

🧠 **Best Practices**
- Use multiple paths and switch dynamically with `GoToNextPatrolGroup()`.
- Ensure all patrol nodes are reachable (navmesh validation).
- Subscribe to events for custom logic (e.g., alarms).

❌ **Common Mistakes & Fixes**
| Issue                     | ❌ Wrong Usage                 | ✅ Correct Usage                       | Explanation                                 |
|--------------------------|-------------------------------|----------------------------------------|---------------------------------------------|
| Guards not patrolling    | Unassigned Patrol Path        | Assign via Details or Assign()        | Path must be assigned to guards             |
| AI can’t reach node      | Nodes through walls/stairs    | Place along valid nav paths           | AI needs navmesh to pathfind                |
| Switching patrols fails  | Group not set/mismatched      | Set Patrol & Next Group in Details    | Required for dynamic patrol transitions     |
| Path always visible      | Show Path left on             | Turn off before publishing            | Avoid visual debug lines in final island    |

📌 **Note:**
- Chain multiple `ai_patrol_path_device`s for dynamic patrols.
- Loop through and control multiple paths via Verse for advanced control.

