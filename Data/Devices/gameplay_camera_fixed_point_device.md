# 📘 gameplay_camera_fixed_point_device – UEFN Verse Device Documentation

## 🔹 Description
The `gameplay_camera_fixed_point_device` is a camera device in Unreal Editor for Fortnite (UEFN) that updates the player’s viewpoint based on a fixed position and rotation in the world. It’s ideal for:
- Cutscenes
- Spawn cinematic shots
- Puzzle perspectives
- Static scene cameras

You can:
- Enable/disable the camera
- Animate or teleport it
- Add/remove it from a player’s camera stack using Verse

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `gameplay_camera_device`
- `gameplay_camera_fixed_point_device`

## 🛠️ Key Methods & Functions
| Method               | Description                                                   |
|----------------------|---------------------------------------------------------------|
| `Enable()`           | Enables the camera (must be enabled for control).             |
| `Disable()`          | Disables the camera device.                                   |
| `AddTo(agent)`       | Adds this camera to the agent’s camera stack.                 |
| `RemoveFrom(agent)`  | Removes this camera from the agent’s camera stack.            |
| `AddToAll()`         | Pushes this camera to all agents’ camera stacks.              |
| `RemoveFromAll()`    | Removes this camera from all agents.                          |
| `GetTransform()`     | Gets the camera’s current transform (location, rotation, scale).|
| `MoveTo(Vector3, Rot, Time)` | Animates the camera to a location/rotation over time.  |
| `TeleportTo(Vector3, Rot)`   | Instantly moves camera to location/rotation.          |

## 🎛 Device Configuration (Details Panel)
| Option              | Description                                                   |
|---------------------|---------------------------------------------------------------|
| Position/Rotation   | Set in the Details panel or via Verse.                        |
| FOV, Look-at Offsets| Control FOV and angle/offset toward targets.                  |
| Enabled             | Enable/disable for camera logic.                              |

## 🛠️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/SpatialMath }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Device to demonstrate gameplay_camera_fixed_point_device control
fixed_point_camera_demo := class(creative_device):

    @editable
    Camera : gameplay_camera_fixed_point_device = gameplay_camera_fixed_point_device{}

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
        EnableButton.InteractedWithEvent.Subscribe(OnEnable)
        DisableButton.InteractedWithEvent.Subscribe(OnDisable)
        AddCameraButton.InteractedWithEvent.Subscribe(OnAddCamera)
        RemoveCameraButton.InteractedWithEvent.Subscribe(OnRemoveCamera)
        MoveCameraButton.InteractedWithEvent.Subscribe(OnMoveCamera)
        TeleportCameraButton.InteractedWithEvent.Subscribe(OnTeleportCamera)

    OnEnable(Agent : agent) : void =
        Camera.Enable()
        Print("Camera enabled")

    OnDisable(Agent : agent) : void =
        Camera.Disable()
        Print("Camera disabled")

    OnAddCamera(Agent : agent) : void =
        Camera.AddTo(Agent)
        Print("Camera added to agent")

    OnRemoveCamera(Agent : agent) : void =
        Camera.RemoveFrom(Agent)
        Print("Camera removed from agent")

    OnMoveCamera(Agent : agent) : void =
        CurrentTransform := Camera.GetTransform()
        NewLocation := CurrentTransform.Translation + vector3{X := 500.0, Y := 0.0, Z := 0.0}
        spawn{Camera.MoveTo(NewLocation, CurrentTransform.Rotation, 1.0)}
        Print("Camera moving forward")

    OnTeleportCamera(Agent : agent) : void =
        CurrentTransform := Camera.GetTransform()
        NewLocation := CurrentTransform.Translation + vector3{X := 0.0, Y := 0.0, Z := 1000.0}
        if (Camera.TeleportTo[NewLocation, CurrentTransform.Rotation]):
            Print("Camera teleported up")
```

## 🧠 How This Works
- **Enable/Disable**: Turns camera logic on/off in your session.
- **AddTo(agent)/RemoveFrom(agent)**: Pushes or pops this camera from a player’s view stack.
- **MoveTo / TeleportTo**: Changes camera position/rotation smoothly or instantly.
- **Button Devices**: Trigger camera actions from player input in the world.

## 📚 How to Use in UEFN
1. **Place Devices in Your Level**
   - Add `gameplay_camera_fixed_point_device`
   - Add button devices for: Enable, Disable, Add, Remove, Move, Teleport

2. **Configure Camera in Details**
   - Adjust position, rotation, FOV, look-at offset

3. **Create and Add Verse Device**
   - Use Verse Explorer: `Create New Verse File` (e.g., `fixed_point_camera_demo.verse`)
   - Paste code, build with `Ctrl+Shift+B`
   - Drag Verse device into your world

4. **Link @editable References**
   - In Details panel, assign:
     - `Camera` → your camera device
     - Buttons → respective button devices

5. **Playtest**
   - Launch Session, test all camera actions interactively

## 🧠 Best Practices
- Use `MoveTo` for smooth cutscenes
- Use `TeleportTo` for instant switches
- Combine with triggers/volumes/timers for cinematic logic
- Remove camera from player stack when switching away

## ❌ Common Issues & Fixes
| Problem                     | Reason                                  | Solution                              |
|-----------------------------|------------------------------------------|----------------------------------------|
| Camera does not activate    | Not enabled or not added to agent stack | Use `Enable()` + `AddTo(agent)`       |
| Camera not moving           | Move/Teleport not called                 | Ensure Verse code triggers the action |
| Camera stuck on player view | Not removed from stack                  | Use `RemoveFrom(agent)`               |

### Notes:
- Effects are scriptable for any agent/group using Verse and device references.
- Most camera logic uses specific subclasses like `gameplay_camera_fixed_point_device`.

