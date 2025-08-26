## 📘 gameplay_camera_first_person_device – UEFN Verse Device Documentation

### 🔹 Description
The `gameplay_camera_first_person_device` is a concrete camera device in Unreal Editor for Fortnite (UEFN) that updates the player’s view to a **true first-person perspective**—directly from their character's head or eyes. This enables immersive gameplay, custom cinematic shots, or first-person-only experiences. You can enable or disable the camera, add or remove it from a player’s viewpoint stack, and animate or teleport its position using Verse.

---

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

---

### 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `gameplay_camera_device`
- `gameplay_camera_first_person_device`

---

### 🛠️ Key Methods & Functions
| Method              | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `Enable()`          | Activates the camera device.                                                |
| `Disable()`         | Deactivates the camera device.                                              |
| `AddTo(agent)`      | Adds this camera to a player's camera stack (makes their view first-person).|
| `RemoveFrom(agent)` | Removes this camera from the player's camera stack.                         |
| `AddToAll()`        | Assigns this camera to all agents.                                          |
| `RemoveFromAll()`   | Removes this camera from all agents.                                        |
| `GetTransform()`    | Returns the current transform of the camera.                                |
| `MoveTo(Vector3, Rot, Time)` | Animates the camera to a location/rotation over time (in seconds).   |
| `TeleportTo(Vector3, Rot)`   | Instantly moves the camera to a location/rotation.                  |

---

### 🎛 Device Configuration (Details Panel)
| Option                 | Description                                           |
|------------------------|-------------------------------------------------------|
| Enabled                | Toggles camera logic for first-person mode.          |
| Assigned To Player     | Set via Verse using `AddTo`/`RemoveFrom`.            |
| FOV/Offsets            | Adjust camera's field of view and position offsets.  |

---

### 🧰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/SpatialMath }
using { /UnrealEngine.com/Temporary/Diagnostics }

first_person_camera_demo := class(creative_device):

    @editable
    Camera : gameplay_camera_first_person_device = gameplay_camera_first_person_device{}

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
        Print("First person camera enabled")

    OnDisable(Agent : agent) : void =
        Camera.Disable()
        Print("First person camera disabled")

    OnAddCamera(Agent : agent) : void =
        Camera.AddTo(Agent)
        Print("First person camera added to agent")

    OnRemoveCamera(Agent : agent) : void =
        Camera.RemoveFrom(Agent)
        Print("First person camera removed from agent")

    OnMoveCamera(Agent : agent) : void =
        CurrentTransform := Camera.GetTransform()
        NewLocation := CurrentTransform.Translation + vector3{X := 500.0, Y := 0.0, Z := 0.0}
        spawn { Camera.MoveTo(NewLocation, CurrentTransform.Rotation, 1.0) }
        Print("First person camera moving forward")

    OnTeleportCamera(Agent : agent) : void =
        CurrentTransform := Camera.GetTransform()
        NewLocation := CurrentTransform.Translation + vector3{X := 0.0, Y := 0.0, Z := 1000.0}
        if (Camera.TeleportTo[NewLocation, CurrentTransform.Rotation]):
            Print("First person camera teleported up")
```

#### Explanation:
- `Camera`: Reference to the placed `gameplay_camera_first_person_device`.
- Button Devices: Trigger functionality via player interactions.

---

### 📦 How to Use in UEFN
1. **Place Devices in Level**
   - Add a `gameplay_camera_first_person_device` to your scene.
   - Place six `button_device` objects for interaction.

2. **Configure in Details Panel**
   - Set physical location, FOV, offsets, and default state.

3. **Create and Add Verse Script**
   - Open **Verse Explorer** → Create new Verse file.
   - Paste code, build script (Ctrl+Shift+B).
   - Drag your Verse actor into the level.

4. **Assign @editable References**
   - In the Details panel:
     - Link the camera and all button devices to the Verse class.

5. **Test in Play Session**
   - Press buttons to switch views, move/teleport the camera.

---

### 🧠 Best Practices
- Ideal for:
  - First-person mini-games
  - Puzzle/horror experiences
  - Cutscenes and zoomed perspectives
- Combine with triggers/events for dynamic camera transitions.

---

### ❌ Common Issues & Fixes
| Problem                           | Possible Cause                    | Solution                                         |
|----------------------------------|----------------------------------|--------------------------------------------------|
| View doesn’t change to first-person | Camera not enabled or not added   | Call `.Enable()` and `.AddTo(agent)`             |
| Camera "stuck"                   | Not removed from player’s stack   | Use `.RemoveFrom(agent)`                         |
| Camera not moving                | Animation method not triggered    | Validate event hookups and input assignments     |

---

### 📌 Notes
- Only concrete subclasses like `gameplay_camera_first_person_device` can be controlled.
- Supports scriptable movements and viewpoint assignments.
- Use with cinematic triggers for advanced gameplay effects.

