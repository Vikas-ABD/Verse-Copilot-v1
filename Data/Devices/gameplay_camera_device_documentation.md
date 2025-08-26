# 📘 gameplay_camera_device – UEFN Verse Device Documentation

## 🔹 Description
The `gameplay_camera_device` (and its subclasses) is used to control or override the player camera’s position, rotation, and perspective in Unreal Editor for Fortnite (UEFN). It can be set to follow fixed points, angles, or orbits for cutscenes, custom spawn views, or special gameplay moments. Camera devices can be enabled/disabled, moved, teleported, or assigned dynamically to a player’s camera stack using Verse.

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

## 🔗 Types & Subclasses
- `gameplay_camera_device` (abstract)
- `gameplay_camera_fixed_point_device`
- `gameplay_camera_fixed_angle_device`
- `gameplay_camera_first_person_device`
- `gameplay_camera_orbit_device`

*(Most use and code samples target specific concrete subclasses, such as `gameplay_camera_fixed_point_device`.)*

## 🛠️ Key Methods & Functions
| Method | Description |
|--------|-------------|
| `Enable()` | Enables the camera device; can be added to player’s camera stack. |
| `Disable()` | Disables the camera device. |
| `AddTo(agent)` | Adds/pushes this camera to the given agent’s camera stack (makes it active). |
| `RemoveFrom(agent)` | Removes/pops this camera from the agent’s stack; restores next camera. |
| `AddToAll()` | Adds camera to all agents. |
| `RemoveFromAll()` | Removes camera from all agents. |
| `GetTransform()` | Returns the current transform (position, rotation). |
| `MoveTo(Vector3, Rot, Time)` | Animates/relocates the camera in world space over time, in seconds. |
| `TeleportTo(Vector3, Rot)` | Instantly teleports camera to new position/rotation. |

## 🧩 Events
*Generally, camera devices do not fire special events but are often combined with triggers, timers, or interaction devices in gameplay.*

## 🎛 Device Configuration (Details Panel)
| Option | Description |
|--------|-------------|
| Camera Type | Fixed point, fixed angle, orbit, or first person. |
| Position/Rotation | Set in world or via Verse. |
| FOV/Other Settings | Some subclasses support FOV, transition, lag. |
| Device Enabled | True/false. |

## 🧰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }
using { /UnrealEngine.com/Temporary/SpatialMath }

gameplay_camera_example := class(creative_device):

    @editable
    CameraDevice : gameplay_camera_fixed_point_device = gameplay_camera_fixed_point_device{}

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
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        AddCameraButton.InteractedWithEvent.Subscribe(OnAddCameraPressed)
        RemoveCameraButton.InteractedWithEvent.Subscribe(OnRemoveCameraPressed)
        MoveCameraButton.InteractedWithEvent.Subscribe(OnMoveCameraPressed)
        TeleportCameraButton.InteractedWithEvent.Subscribe(OnTeleportCameraPressed)

    OnEnablePressed(Agent : agent) : void =
        CameraDevice.Enable()
        Print("Camera device enabled!")

    OnDisablePressed(Agent : agent) : void =
        CameraDevice.Disable()
        Print("Camera device disabled!")

    OnAddCameraPressed(Agent : agent) : void =
        CameraDevice.AddTo(Agent)
        Print("Camera added to agent!")

    OnRemoveCameraPressed(Agent : agent) : void =
        CameraDevice.RemoveFrom(Agent)
        Print("Camera removed from agent!")

    OnMoveCameraPressed(Agent : agent) : void =
        CurrentTransform := CameraDevice.GetTransform()
        NewLocation := CurrentTransform.Translation + vector3{X := 500.0, Y := 0.0, Z := 0.0}
        spawn{CameraDevice.MoveTo(NewLocation, CurrentTransform.Rotation, 1.0)}
        Print("Camera moved forward!")

    OnTeleportCameraPressed(Agent : agent) : void =
        CurrentTransform := CameraDevice.GetTransform()
        NewLocation := CurrentTransform.Translation + vector3{X := 0.0, Y := 0.0, Z := 1000.0}
        if (CameraDevice.TeleportTo[NewLocation, CurrentTransform.Rotation]):
            Print("Camera teleported up!")
```

## 🧠 Best Practices
- Use timed/triggers, sequencing, and removal/addition for cutscenes, dramatic zoom/angle changes, checkpoint cams, or lobby scenes.
- Use camera device override for unique perspectives or “spectator” modes.
- Script transitions using `MoveTo` for smooth, cinematic effects.

## ❌ Common Issues & Fixes
| Problem | Reason | Solution |
|---------|--------|----------|
| Camera does not activate | Not enabled/not `AddTo()` called | Call `.Enable()` and then `.AddTo(agent)` |
| View not switched | Not added for correct Agent | Look up correct agent for targeted effect |
| Rotation/position issues | Transform not set/moved | Use `MoveTo`, `TeleportTo`, or `SetTransform` as needed |

## 📌 Notes
- Cameras can be assigned to specific players (agents) using `AddTo(agent)`, and removed with `RemoveFrom(agent)`.
- Subclass (such as orbit/angle/fixed) determines the effect; all share the above core control methods.
- Combine Verse code with triggers, timers, or player actions for cutscene, narrative, or gameplay camera control.

