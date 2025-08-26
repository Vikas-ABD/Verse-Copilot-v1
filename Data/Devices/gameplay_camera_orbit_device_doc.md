# gameplay_camera_orbit_device – UEFN Verse Device Documentation

## 🔹 Description
The `gameplay_camera_orbit_device` is a camera device in Unreal Editor for Fortnite (UEFN) that follows a target player character from a set distance. It allows players to manually rotate (orbit) the view around themselves, supporting dynamic third-person perspectives. This device is commonly used for over-the-shoulder, follow, or adventure-style camera systems and is fully controllable via Verse scripting or device actions.

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `gameplay_camera_device`
- `gameplay_camera_orbit_device`

## 🛠️ Key Methods & Functions
| Method              | Description                                                    |
|---------------------|----------------------------------------------------------------|
| `Enable()`          | Activates the orbit camera device for use.                    |
| `Disable()`         | Deactivates the orbit camera device.                          |
| `AddTo(agent)`      | Adds this orbital camera to a specific player's camera stack.  |
| `RemoveFrom(agent)` | Removes the camera from a player’s camera stack.              |
| `AddToAll()`        | Applies the camera to all players.                            |
| `RemoveFromAll()`   | Removes the camera from all players.                          |
| `GetTransform()`    | Gets the current position and rotation of the camera.         |
| `MoveTo(Vector3, Rot, Time)` | Animates camera movement and rotation over time.      |
| `TeleportTo(Vector3, Rot)`   | Instantly moves camera to a position and rotation.    |

## 🎛 Device Configuration (Details Panel)
- **Distance/Offset**: Set follow distance, offset, and vertical positioning.
- **FOV**: Field of View.
- **Angle Restrictions**: Min/max vertical and horizontal orbit angles.
- **Enable/Disable**: Set initial enabled state.

## 🛠️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/SpatialMath }
using { /UnrealEngine.com/Temporary/Diagnostics }

orbit_camera_demo := class(creative_device):

    @editable
    Camera : gameplay_camera_orbit_device = gameplay_camera_orbit_device{}

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
        Print("Orbit camera enabled")

    OnDisable(Agent : agent) : void =
        Camera.Disable()
        Print("Orbit camera disabled")

    OnAddCamera(Agent : agent) : void =
        Camera.AddTo(Agent)
        Print("Orbit camera added to agent")

    OnRemoveCamera(Agent : agent) : void =
        Camera.RemoveFrom(Agent)
        Print("Orbit camera removed from agent")

    OnMoveCamera(Agent : agent) : void =
        CurrentTransform := Camera.GetTransform()
        NewLocation := CurrentTransform.Translation + vector3{X := 500.0, Y := 0.0, Z := 0.0}
        spawn{Camera.MoveTo(NewLocation, CurrentTransform.Rotation, 1.0)}
        Print("Orbit camera moving forward")

    OnTeleportCamera(Agent : agent) : void =
        CurrentTransform := Camera.GetTransform()
        NewLocation := CurrentTransform.Translation + vector3{X := 0.0, Y := 0.0, Z := 1000.0}
        if (Camera.TeleportTo[NewLocation, CurrentTransform.Rotation]):
            Print("Orbit camera teleported up")
```

## 🧠 Explanation
- **Camera**: Reference to the placed `gameplay_camera_orbit_device`.
- **Buttons**: Trigger specific actions:
  - `Enable/Disable`: Toggles the orbit camera device.
  - `AddTo/RemoveFrom`: Adds/removes the camera to/from an agent.
  - `Move/Teleport`: Animates or snaps the camera position.
- **Rotation**: Players can manually rotate the camera during gameplay.

## ✨ How to Use in UEFN
1. **Place Devices in Your Level**:
   - Add a `gameplay_camera_orbit_device`.
   - Place six `button_device` instances: Enable, Disable, Add Camera, Remove Camera, Move Camera, Teleport Camera.

2. **Configure Orbit Camera (Details Panel)**:
   - Adjust follow distance, offsets, FOV, and angle restrictions.

3. **Create and Add Verse Script**:
   - In **Verse Explorer**, right-click folder > *Create New Verse File*.
   - Paste the example code and build (Ctrl+Shift+B).
   - Drag the Verse device actor into the level.

4. **Assign `@editable` References**:
   - In the Verse device’s Details panel:
     - Set `Camera` to your orbit device.
     - Link each button field to the respective button device.

5. **Test and Play**:
   - Start the session and interact with buttons to control the orbit camera.

## 🧠 Best Practices
- Use `MoveTo`/`TeleportTo` for cinematic transitions.
- Enable/disable and AddTo/RemoveFrom to control camera stages.
- Integrate with triggers/sequencers for custom camera behaviors.

## ❌ Common Issues & Fixes
| Issue                    | Cause                         | Solution                                 |
|--------------------------|-------------------------------|------------------------------------------|
| Camera doesn’t activate | Not enabled/added to stack     | Call `.Enable()` then `.AddTo(agent)`    |
| View doesn’t update     | Not moved or stack conflict   | Use proper methods/avoid overlap         |
| Can’t orbit             | Camera not in stack/view       | Ensure `.AddTo(agent)` worked            |

## 💡 Notes
- Orbit camera views are ideal for third-person perspectives.
- Combine with fixed or FPS views for hybrid systems.
- Script logic is per-agent, allowing player-specific camera control.
- Nearly identical setup as other camera device types.

