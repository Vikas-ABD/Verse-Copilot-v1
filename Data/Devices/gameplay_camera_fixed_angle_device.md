📘 gameplay_camera_fixed_angle_device – UEFN Verse Device Documentation

🔹 Description
The gameplay_camera_fixed_angle_device is a camera device in Unreal Editor for Fortnite (UEFN) that forces the player’s camera to a fixed world position and rotation—perfect for puzzles, platformers, boss arenas, boss cams, or any fixed-angle cutscene. You have full Verse script access to enable/disable, move, or assign this camera to any agent/player at runtime.

🧱 Verse Using Statement
verse
using { /Fortnite.com/Devices }

🔗 Inheritance Hierarchy
* creative_object
* creative_device_base
* gameplay_camera_device
* gameplay_camera_fixed_angle_device

🛠️ Key Methods & Functions
| Method | Description |
|--------|-------------|
| Enable() | Enables this camera device, allowing view override. |
| Disable() | Disables this camera device. |
| AddTo(agent) | Pushes this camera onto a player’s camera stack (making it active for them). |
| RemoveFrom(agent) | Removes this camera from the player’s stack. |
| AddToAll() | Pushes to all agents at once. |
| RemoveFromAll() | Pops from all stacks at once. |
| GetTransform() | Returns the camera’s current transform (location/rotation). |
| MoveTo(Vector3, Rot, Time) | Animates camera to a new location/rotation over time, in seconds. |
| TeleportTo(Vector3, Rot) | Instantly moves camera to a target point/rotation. |

🎛 Device Configuration (Details Panel)
| Option | Description |
|--------|-------------|
| Position/Rotation | Set fixed location/angle in Details or via Verse. |
| Enabled | Whether the camera is initially active. |
| Angle/FOV | Controls the camera’s orientation and field of view. |

🧰 Verse Usage Example
Below is a complete example showing control of a fixed angle camera device using buttons (enable/disable/add/remove/move/teleport):

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/SpatialMath }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Device to demonstrate gameplay_camera_fixed_angle_device control
fixed_angle_camera_demo := class(creative_device):

    @editable
    Camera : gameplay_camera_fixed_angle_device = gameplay_camera_fixed_angle_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    AddCameraButton : button_device = button_device{}

    @editable
    RemoveCameraButton : button_device = button_device{}

    @editable
    MoveCameraButton : button_device = button_device{}

    @editable
    TeleportCameraButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        # Subscribe to button events
        EnableButton.InteractedWithEvent.Subscribe(OnEnable)
        DisableButton.InteractedWithEvent.Subscribe(OnDisable)
        AddCameraButton.InteractedWithEvent.Subscribe(OnAddCamera)
        RemoveCameraButton.InteractedWithEvent.Subscribe(OnRemoveCamera)
        MoveCameraButton.InteractedWithEvent.Subscribe(OnMoveCamera)
        TeleportCameraButton.InteractedWithEvent.Subscribe(OnTeleportCamera)

    # Button event handlers
    OnEnable(Agent : agent) : void =
        Camera.Enable()
        Print("Fixed angle camera enabled")

    OnDisable(Agent : agent) : void =
        Camera.Disable()
        Print("Fixed angle camera disabled")

    OnAddCamera(Agent : agent) : void =
        Camera.AddTo(Agent)
        Print("Fixed angle camera added to agent")

    OnRemoveCamera(Agent : agent) : void =
        Camera.RemoveFrom(Agent)
        Print("Fixed angle camera removed from agent")

    OnMoveCamera(Agent : agent) : void =
        # Move camera 500 units forward over 1 second
        CurrentTransform := Camera.GetTransform()
        NewLocation := CurrentTransform.Translation + vector3{X := 500.0, Y := 0.0, Z := 0.0}
        spawn{Camera.MoveTo(NewLocation, CurrentTransform.Rotation, 1.0)}
        Print("Fixed angle camera moving forward")

    OnTeleportCamera(Agent : agent) : void =
        # Teleport camera 1000 units up
        CurrentTransform := Camera.GetTransform()
        NewLocation := CurrentTransform.Translation + vector3{X := 0.0, Y := 0.0, Z := 1000.0}
        if (Camera.TeleportTo[NewLocation, CurrentTransform.Rotation]):
            Print("Fixed angle camera teleported up")
```

How this works:
* Enable/Disable: Turns the camera scripting logic on/off.
* Add/Remove: Attaches or detaches the camera view for a player at runtime.
* MoveTo/TeleportTo: Shifts the camera instantly (teleport) or smoothly (move) to new world space positions and angles.
* All button devices must be placed and referenced in the Verse device’s Details panel.

How to Use in UEFN
1. Place Devices in Your Level
* Add a gameplay_camera_fixed_angle_device in your world (Devices > Camera).
* Add six button_devices for Enable, Disable, Add, Remove, Move, and Teleport controls.

2. Configure Camera in Details Panel
* Set the camera’s original position, rotation, field of view, and “Enabled” status to suit your gameplay.

3. Create and Add Verse Script
* In Verse Explorer:
  – Right-click folder → Create New Verse File (e.g., fixed_angle_camera_demo.verse)
  – Create Empty, paste the provided code, save.
* Build Verse code (Ctrl+Shift+B) until “Build Succeeded.”
* Place your custom Verse device in the world.

4. Assign Editable References
* In your Verse device’s Details, assign:
  * Camera: your fixed angle camera device
  * All Button fields: to your button devices in the level

5. Playtest!
* Interact with the buttons to test enabling, switching, and moving/teleporting the camera on players.

🧠 Best Practices
* Use for puzzle platforms, boss fights, side-scrolling areas, or to present dramatic/world angles.
* Combine MoveTo for cinematic sweeps and TeleportTo for instantaneous viewpoint changes.
* Script camera transitions using triggers, timelines, or button devices for full experience control.

❌ Common Issues & Fixes
| Problem | Likely Cause | Solution |
|---------|---------------|----------|
| Camera not switching | Not enabled, or AddTo not called | Use .Enable() and .AddTo(agent) |
| View not restored | Not removing camera from stack | Use .RemoveFrom(agent) at right time |
| No animated movement | Only calling TeleportTo | Use .MoveTo() for smooth transitions |

Note:
* You must reference the fixed angle camera to your Verse device and ensure all required buttons are linked in the Details panel for live play control.
* Subclass is for “fixed angle” views. For fixed points or orbits, use their respective device types.
* All camera scripting is runtime and per-agent—supports both solo and multiplayer experiences.

