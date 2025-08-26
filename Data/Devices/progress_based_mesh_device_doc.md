## progress_based_mesh_device – UEFN Verse Device Documentation

### 🔹 Description
The `progress_based_mesh_device` is a visual gameplay device in Unreal Editor for Fortnite (UEFN) that transitions between multiple meshes based on a progression value. As the device’s progression changes (increases or decreases), it automatically swaps its visible mesh (and optionally material) at configured threshold values. This makes it ideal for creating dynamic growth mechanics, progress bars, filling containers, decaying objects, and similar visual systems.

---

### 🧱 Imports Required
```verse
verse
using { /Fortnite.com/Devices }
```

---

### 🔗 Inheritance Hierarchy
- `creative_object`: Base class for creative devices and props.
- `creative_device_base`: Base class for creative_device.
- `progress_based_mesh_device`: Inherits from creative_device_base.

---

### 🧹 Data Members
| Name | Type | Description |
|------|------|-------------|
| `CurrentProgress` | ?float | Current progression value (clamped between 0 and `ProgressTarget`). Updating triggers mesh transitions. |
| `ProgressTarget` | ?float | Progress goal (default max 100). Changing this clamps `CurrentProgress`. |
| `ProgressRate` | ?float | Rate of increase per second when in Progress state. |
| `RegressRate` | ?float | Rate of decrease per second when in Regress state. |
| `ProgressState` | ?progress_device_state | Current update/transition state: Progress, Regress, or Pause. |
| `ThresholdMesh` | *(Editor-set)* | Defines which mesh appears at which thresholds. Set in UEFN Details panel (Visuals > ThresholdMeshes). |

---

### 📡 Key Events
| Event | Description |
|-------|-------------|
| `EmptyEvent` | Fired when `CurrentProgress` reaches 0. |
| `FillEvent` | Fired when `CurrentProgress` reaches `ProgressTarget`. |
| `ProgressChangeEvent` | Fired on any change to `CurrentProgress`. |
| `ProgressThresholdCrossEvent` | Fired when a new threshold is crossed and the mesh is changed. |

---

### 🧰 Core Methods (Inherited)
| Method Signature | Description |
|------------------|-------------|
| `GetTransform(): transform` | Get the device’s transform (position, rotation, scale). |
| `MoveTo(Position: vector3, Rotation: rotation, Time: float)` | Smoothly move to a new position. |
| `MoveTo(TargetTransform: transform, Time: float)` | Smoothly move using a transform. |
| `TeleportTo(Position: vector3, Rotation: rotation)` | Instantly teleport to a new position/rotation. |
| `TeleportTo(TargetTransform: transform)` | Instantly teleport via transform. |

---

### 🚦 Progress States (progress_device_state enum)
- `Progress`: Progressing toward `ProgressTarget` at `ProgressRate`.
- `Regress`: Regressing toward 0 at `RegressRate`.
- `Pause`: Paused, does not change automatically.

---

### 🚩 Usage Example
```verse
using { /Fortnite.com/Devices }

progression_manager := class(creative_device):

    @editable
    ProgressMesh : progress_based_mesh_device = progress_based_mesh_device{}

    OnBegin<override>()<suspends> : void =
        # Manually set progress to 50
        set ProgressMesh.CurrentProgress = 50.0

        # Start progressing
        set ProgressMesh.ProgressState = progress_device_state.Progress

        # Listen for progression events
        ProgressMesh.ProgressChangeEvent.Subscribe(OnProgressChanged)
        ProgressMesh.ProgressThresholdCrossEvent.Subscribe(OnThresholdCrossed)

    OnProgressChanged(Payload:payload):void =
        Print("Progress changed!")

    OnThresholdCrossed(Payload:payload):void =
        Print("Mesh threshold crossed!")
```

---

### 🧠 Best Practices
- Set up `ThresholdMeshes` in the UEFN Details panel (Visuals > ThresholdMeshes) for visual transitions.
- Adjust `ProgressTarget`, `ProgressRate`, and `RegressRate` based on your game logic.
- Use `ProgressState` in Verse to start/stop progression, or directly modify `CurrentProgress` for immediate changes.
- Subscribe to `ProgressChangeEvent` and `ProgressThresholdCrossEvent` for adding effects or logic.
- Ideal for simulating growth, decay, filling, progress bars, and resource indicators.

---

### ❌ Incorrect Usage Examples and Fixes
| Issue | ❌ Wrong Example | ✅ Correct Example | Explanation |
|-------|-------------------|------------------------|-------------|
| Ignoring setup | Not setting ThresholdMeshes | Set in UEFN Details panel (Visuals > ThresholdMeshes) | No mesh transition otherwise |
| Assigning out-of-bounds | `set ProgressMesh.CurrentProgress = 150.0` | `set ProgressMesh.CurrentProgress = Min(100.0, DesiredValue)` | Value is clamped automatically |
| Using before assigning | Using `ProgressMesh` before setting it | Assign in Details panel using `@editable` | Prevents `nil` reference errors |

---

### 📅 Notes
- Threshold mesh transitions must be configured in the UEFN editor (Visuals > ThresholdMeshes).
- Progression is controlled through Verse or gameplay logic (e.g., triggers, timers).
- Use events for syncing audio, visuals, or gameplay logic with progression state.

