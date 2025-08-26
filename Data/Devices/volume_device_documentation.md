📘 **volume_device – UEFN Verse Device Documentation**

---

🔹 **Description**

The `volume_device` defines a 3D space within a Fortnite island to detect when agents (players or controllable entities) enter or exit the area. Common use cases include:

- Zone triggers
- Region-based logic
- Safe zones
- Region-specific scoring
- Mission progression

You can respond to entry/exit events in Verse or via device wiring.

---

🧱 **Verse Using Statement**
```verse
using { /Fortnite.com/Devices }
```

---

🔗 **Inheritance Hierarchy**

- `creative_object`
  - `creative_device_base`
    - `volume_device`

---

🧩 **Data Members (Events)**

| Name               | Type                | Description                                   |
|--------------------|---------------------|-----------------------------------------------|
| AgentEntersEvent   | listenable(agent)   | Signaled when an agent enters the volume      |
| AgentExitsEvent    | listenable(agent)   | Signaled when an agent exits the volume       |
| PropEnterEvent     | listenable(prop)    | Signaled when a creative prop enters volume   |
| PropExitEvent      | listenable(prop)    | Signaled when a creative prop exits volume    |

---

🛠️ **Functions & Methods**

| Name                | Signature                               | Description                                                      |
|---------------------|------------------------------------------|------------------------------------------------------------------|
| IsInVolume          | (Agent: agent) <decides>: void           | Checks if a specific agent is in the volume                      |
| GetAgentsInVolume   | (): []agent                              | Returns a list of all agents currently inside the volume         |
| GetTransform        | <transacts>: transform                   | Returns the world transform (position/rotation/scale)            |
| MoveTo              | (Position, Rotation, Time)               | Moves device to new position/rotation over time                  |
| MoveTo              | (Transform, Time)                        | Moves device to new transform over time                          |
| TeleportTo          | (Position, Rotation)                     | Instantly teleports device to specified position/rotation        |
| TeleportTo          | (Transform)                              | Instantly teleports device to specified transform                |

---

🎛 **Configuration Options (Details Panel)**

- **Volume Shape**: Choose cube, sphere, capsule, or custom mesh
- **Size/Radius**: Define volume size
- **Enable Volume at Start**: Automatically turn on at game start
- **Team/Class Filters**: Filter which agents are detected
- **Show Visualization**: Enable for volume size visualization

---

🧰 **Usage Example**

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

volume_tracking_example := class(creative_device):

    @editable
    Volume : volume_device = volume_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        Volume.AgentEntersEvent.Subscribe(OnAgentEnters)
        Volume.AgentExitsEvent.Subscribe(OnAgentExits)
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    OnAgentEnters(Agent : agent) : void =
        Print("Agent entered the volume!")
        if (Volume.IsInVolume[Agent]):
            Print("Confirmed: Agent is in the volume.")

    OnAgentExits(Agent : agent) : void =
        Print("Agent exited the volume!")
        AgentsInVolume := Volume.GetAgentsInVolume()
        Print("Agents currently in volume: {AgentsInVolume.Length}")

    OnEnablePressed(Agent : agent) : void =
        Print("Volume cannot be enabled/disabled directly.")

    OnDisablePressed(Agent : agent) : void =
        Print("Volume cannot be enabled/disabled directly.")
```

---

🧠 **Best Practices**

- Ensure the volume is properly sized and placed
- Use entry/exit events for scoring, effects, or mission logic
- Apply Team/Class filters to restrict interactions
- Recalculate logic if volume position is changed at runtime

---

❌ **Incorrect Usage Examples and Fixes**

| Issue                             | ❌ Wrong                                 | ✅ Correct                                               | Explanation                                                              |
|----------------------------------|------------------------------------------|----------------------------------------------------------|--------------------------------------------------------------------------|
| Device not enabled               | Not enabled                              | Set “Enable Volume at Start” or call `.Enable()`         | Device must be active to detect agents                                  |
| Not subscribing to events        | No event handling                        | Use `AgentEntersEvent.Subscribe()`                        | Events must be explicitly subscribed to                                 |
| Incorrect team/class setup       | All agents trigger events                | Set Team/Class filters                                    | Prevents triggering by unintended agents                                |
| Moving volume without logic update | Teleport/Move without logic refresh     | Recalculate logic if needed                              | Keeps spatial logic accurate                                            |

---

📌 **Note**

- Ideal for creating safe zones, event triggers, and quest areas
- Combine with scoreboard, spawner, damage, or VFX devices
- Use async or spawn expressions in Verse for reliable event timing

