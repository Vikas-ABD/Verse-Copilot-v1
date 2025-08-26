📘 **chair_device – UEFN Verse Device Documentation**

🔹 **Description**
The `chair_device` creates a chair in your Fortnite experience where players (agents) can sit and optionally stand up. Ideal for scenes like cinemas, concerts, waiting areas, terminals, or any interactive seating mechanic. You can control when agents can enter or exit, and respond to sit/stand events in Verse.

🧱 **Verse Using Statement**
```verse
using { /Fortnite.com/Devices }
```

🔗 **Inheritance Hierarchy**
- creative_object
- creative_device_base
- chair_device

🧩 **Data Members (Events)**
| Name          | Type               | Description                               |
|---------------|--------------------|-------------------------------------------|
| SeatedEvent   | listenable(agent)  | Fires when an agent sits on the chair.    |
| ExitedEvent   | listenable(agent)  | Fires when an agent stands/exits the chair.|

🛠️ **Functions & Methods**
| Name                | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| Enable()            | Enables the chair for interaction/seating.                                 |
| Disable()           | Disables the chair; sitting is not possible and any seated agent will be ejected. |
| EnableExit()        | Allows any seated agent to leave the chair manually.                        |
| DisableExit()       | Prevents agents from leaving manually; use `Eject()` to force exit.         |
| Seat(Agent)         | Makes the specified agent sit on the chair (if allowed/possible).           |
| Eject()             | Forces any agent currently in the chair to leave.                           |
| Eject(Agent)        | Forces a specified agent to exit the chair if seated.                       |
| IsSeated(Agent)     | Succeeds if agent is currently seated in this chair.                        |
| IsOccupied()        | Succeeds if chair is currently occupied.                                    |
| GetSeatedAgent()    | Returns the agent currently occupying the chair (if any).                   |

🎛 **Configuration Options (Details Panel)**
- **Chair Model**: Choose style: Invisible, Comfy Chair, Barstool, Barrel, Stone, Basic, Custom (UEFN only).
- **Interact Time/Radius/Angle**: Control how players interact and from what distance/direction.
- **Activating Team/Class**: Restrict who may sit in the chair.
- **Enabled During Game**: If on, available at match start; if off, must be enabled with Verse/event.
- **Player Exit Enabled**: If on, players can stand up on their own.
- **Camera Collision/Audio/Prompt Text**: Customize camera, SFX, and prompts.

🧰 **Verse Usage Example**
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

chair_device_example := class(creative_device):

    @editable
    Chair : chair_device = chair_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    EnableExitButton : button_device = button_device{}

    @editable
    DisableExitButton : button_device = button_device{}

    @editable
    SitButton : button_device = button_device{}

    @editable
    EjectButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        Chair.SeatedEvent.Subscribe(OnAgentSeated)
        Chair.ExitedEvent.Subscribe(OnAgentExited)

        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        EnableExitButton.InteractedWithEvent.Subscribe(OnEnableExitPressed)
        DisableExitButton.InteractedWithEvent.Subscribe(OnDisableExitPressed)
        SitButton.InteractedWithEvent.Subscribe(OnSitPressed)
        EjectButton.InteractedWithEvent.Subscribe(OnEjectPressed)

    OnAgentSeated(Agent : agent) : void =
        Print("Agent sat on the chair!")

    OnAgentExited(Agent : agent) : void =
        Print("Agent exited the chair!")

    OnEnablePressed(Agent : agent) : void =
        Chair.Enable()
        Print("Chair enabled!")

    OnDisablePressed(Agent : agent) : void =
        Chair.Disable()
        Print("Chair disabled!")

    OnEnableExitPressed(Agent : agent) : void =
        Chair.EnableExit()
        Print("Chair exit enabled!")

    OnDisableExitPressed(Agent : agent) : void =
        Chair.DisableExit()
        Print("Chair exit disabled!")

    OnSitPressed(Agent : agent) : void =
        Chair.Seat(Agent)
        Print("Button pressed: forced Agent to sit!")

    OnEjectPressed(Agent : agent) : void =
        Chair.Eject()
        Print("Eject called: any agent in chair was ejected!")
```

🔧 **How it works in UEFN**
1. **Place Devices in Level**
    - Add a `chair_device` at each spot you want seating in your level.
    - Add `button_device`s for controlling enable, disable, force sit, eject, and exit.

2. **Configure in Details Panel**
    - Choose chair model, visuals, and whether player exit is enabled.
    - Restrict to teams/classes, set interact settings, and prompt text.

3. **Create & Build Verse Device**
    - Add a new Verse file (e.g., `chair_device_example.verse`), paste in the code, and save.
    - Build the code using "Build Verse Code" or `CTRL+SHIFT+B`.

4. **Place and Connect Devices**
    - Drag the Verse device into your map.
    - Assign references in the Details panel.

5. **Test**
    - Launch a session, interact with the chair and control buttons, and observe events.

🧠 **Best Practices**
- Use `EnableExit` and `DisableExit` for controlled sequences like cutscenes.
- Use `SeatedEvent` and `ExitedEvent` for triggering sequences, effects, or rewards.
- Use `Seat(agent)` for cutscenes or events where players must be seated.
- Set `Enabled During Game = Off` and control activation via Verse.

❌ **Common Mistakes & Fixes**
| Issue                  | ❌ Wrong Usage                      | ✅ Correct Usage                                     | Explanation                                      |
|------------------------|-------------------------------------|-----------------------------------------------------|--------------------------------------------------|
| Agent can’t leave      | Player Exit Enabled = Off          | Call `EnableExit()` in Verse or set option On       | Toggle with Verse or control buttons             |
| Anyone can sit         | No team/class restriction set      | Set Activating Team/Class as needed in Details      | Restricts access to certain players              |
| Chair does nothing     | Device not enabled                 | Call `Enable()` in Verse or set enabled at start    | Must be enabled to be usable                    |
| Trying to eject empty  | Call `Eject()` while chair empty  | Safe call, but will only eject if occupied          | Code safe, but has no effect if chair is empty   |

📌 **Note**:
- Custom meshes work only when Chair Model = Custom.
- Use multiple chair devices for synchronized experiences.
- Use `IsSeated`, `IsOccupied`, and `GetSeatedAgent()` for gameplay logic.

