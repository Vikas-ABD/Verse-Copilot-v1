## creative\_prop – UEFN Verse Device Documentation

### 🔹 Description

The `creative_prop` class represents any Fortnite prop that has been placed or spawned on your island. It extends from `creative_object`, inheriting transform and movement utilities, and adds capabilities such as damage control, visibility toggling, mesh and material changes, and destruction.

This class is ideal for dynamically interactive props such as destructibles, moving objects, puzzle components, and more. It also implements the `invalidatable` interface, meaning it can become invalid or disposed of during gameplay.

---

### 🧱 Imports Required

```verse
using { /Fortnite.com/Devices }
```

---

### 🔁 Main Event

`creative_prop` does not expose any listenable events by default. However, lifecycle and state can be handled via methods like `IsValid()` and `IsDisposed()`.

**✅ Lifecycle Hook:**

```verse
OnBegin<override>(): void =
    Print("Creative prop ready!")
```

---

### 🧰 Core Methods

| Method Signature                                                      | Description                                                                                                             |
| --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `Dispose(): void`                                                     | Destroys the prop and removes it from the world.                                                                        |
| `IsDisposed(): logic`                                                 | Returns true if the prop has already been disposed or destroyed.                                                        |
| `IsValid(): logic`                                                    | Returns true if the prop is currently valid and usable in-game. Always check before using movement or visual functions. |
| `GetTransform(): transform`                                           | Gets the prop's current location, rotation, and scale (in cm). Use only after checking `IsValid()`.                     |
| `MoveTo(Position: vector3, Rotation: rotation, Time: float): void`    | Smoothly moves and rotates the prop over time.                                                                          |
| `MoveTo(TargetTransform: transform, Time: float): void`               | Moves the prop using a full transform object.                                                                           |
| `TeleportTo(Position: vector3, Rotation: rotation): void`             | Instantly teleports and rotates the prop.                                                                               |
| `TeleportTo(TargetTransform: transform): void`                        | Instantly teleports using a full transform.                                                                             |
| `Hide(): void`                                                        | Hides the prop in the world and disables collisions.                                                                    |
| `Show(): void`                                                        | Shows the prop and enables collisions again.                                                                            |
| `SetMesh(NewMesh: mesh): void`                                        | Changes the mesh used by this prop instance.                                                                            |
| `SetMaterial(MaterialToApply: material, ElementIndex: int = 0): void` | Changes the material of the mesh. Optionally specify the element index.                                                 |

---

### 🧬 Data Members

| Property       | Type   | Description                                                                   |
| -------------- | ------ | ----------------------------------------------------------------------------- |
| `CanBeDamaged` | ?logic | Controls whether the prop can take damage. If false, it becomes invulnerable. |

---

### 🚦 Common Usage: Step-by-Step Example

```verse
using { /Fortnite.com/Devices }

my_prop_script := class(MyProp: creative_prop):

    OnBegin<override>() :=
        if (MyProp.IsValid()):
            MyProp.Show()  # Ensure visible
            MyProp.CanBeDamaged = true  # Make destructible
            var start := MyProp.GetTransform()

            # Move the prop upward smoothly
            var targetPos := start.Translation + vector3{Z := 200.0}
            MyProp.MoveTo(targetPos, start.Rotation, 1.5)
```

---

### ❌ Incorrect Usage Examples and How to Fix

| Issue                                      | ❌ Wrong                                     | ✅ Fix                                                        |
| ------------------------------------------ | ------------------------------------------- | ------------------------------------------------------------ |
| Calling transform without checking         | `MyProp.GetTransform()`                     | `if (MyProp.IsValid()): MyProp.GetTransform()`               |
| Trying to apply material to a missing mesh | `MyProp.SetMaterial(SomeMaterial)`          | Ensure the prop has a valid mesh before changing material    |
| Using `MoveTo()` after `Dispose()`         | `MyProp.Dispose(); MyProp.MoveTo(...)`      | Check `IsDisposed()` or avoid calling after disposal         |
| Forgetting to show a hidden prop           | Expecting a hidden prop to be visible again | Call `MyProp.Show()` after `Hide()` to make it visible again |

---

### 🧠 Best Practices

- Always check `IsValid()` and/or `IsDisposed()` before manipulating the prop.
- Use `Hide()` and `Show()` to animate props appearing/disappearing in puzzles or story events.
- Set `CanBeDamaged` to `false` for invulnerable props (e.g., environmental decor).
- Use `Dispose()` carefully to permanently remove props mid-game.
- Combine `SetMaterial()` with logic events for visual feedback (e.g., color change on interaction).
- Use `SetMesh()` to switch prop appearance dynamically during gameplay.

---

### 🎯 Great for:

- Destructible or damageable props
- Puzzle elements (e.g. toggling appearance or state)
- Environmental storytelling (props changing mesh or material)
- Dynamic movement, teleportation, and visual scripting
- Disappearing/reappearing world objects

