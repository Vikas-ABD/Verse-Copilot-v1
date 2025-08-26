# 📦 `base_item_spawner_device` – UEFN Verse Device Documentation

---

## 🔹 Description

The `base_item_spawner_device` is a foundational class in UEFN (Unreal Editor for Fortnite) that represents any device capable of spawning in-game items for players. It provides core functionality such as:

- Enabling/disabling the spawner
- Responding to item pickups
- Managing spatial transformations like movement or teleportation

> ⚙️ **Note:** Do not use this class directly unless you are extending it. Use derived classes like `item_spawner_device` or `random_item_spawner_device` for practical purposes.

---

## 🔗 Inheritance Hierarchy

```text
creative_object
└── creative_device_base
    └── base_item_spawner_device
```

### 🔸 Parent Classes

- **creative\_object**: Base for all in-world creative objects (props, devices).
- **creative\_device\_base**: Provides creative device behaviors such as enabling/disabling.

---

## 📅 Required Imports

```verse
using { /Fortnite.com/Devices }
```

---

## 🤩 Data Members

| Name              | Type              | Description                                                                            |
| ----------------- | ----------------- | -------------------------------------------------------------------------------------- |
| ItemPickedUpEvent | listenable(agent) | Event triggered when an item is picked up. Sends the agent (player) that picked it up. |

> 📣 Use this to trigger custom logic when players collect spawned items.

---

## 🧰 Functions

### ✅ Enable / Disable

| Function  | Description                                          |
| --------- | ---------------------------------------------------- |
| Enable()  | Activates the spawner so it can spawn items.         |
| Disable() | Deactivates the spawner. Items will no longer spawn. |

---

### 🛍️ Positioning and Movement

#### 📦 Transform Management

| Function       | Description                                                                                |
| -------------- | ------------------------------------------------------------------------------------------ |
| GetTransform() | Returns the current world transform (location, rotation, scale) of the device in cm units. |

> 🔐 Be sure to call `IsValid()` first to avoid runtime errors if the device is destroyed.

#### 🚚 Movement (Animated)

| Function Signature               | Description                                                                        |
| -------------------------------- | ---------------------------------------------------------------------------------- |
| MoveTo(Position, Rotation, Time) | Smoothly moves the spawner to a target position/rotation over a duration.          |
| MoveTo(Transform, Time)          | Moves the spawner to a specific transform (location + rotation + scale) over time. |

> 💡 Any currently playing animation will be interrupted and canceled.

#### 🪄 Instant Teleportation

| Function Signature             | Description                                                        |
| ------------------------------ | ------------------------------------------------------------------ |
| TeleportTo(Position, Rotation) | Instant teleport to specified location and orientation.            |
| TeleportTo(Transform)          | Instant teleport using full transform (position, rotation, scale). |

---

## 🧪 Example Usage

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

my_item_spawner := class(creative_device):

    @editable
    Spawner : base_item_spawner_device = base_item_spawner_device{}

    OnBegin<override>()<suspends> : void =
        Spawner.Enable()
        Spawner.ItemPickedUpEvent.Subscribe(OnItemPickup)

    OnItemPickup(Player : agent) : void =
        Print("Item picked up by: {Player.GetPlayerName()}")
```

---

## ⚠️ Important Notes

- This is a base class. You’ll likely be using a subclass like:
  - `item_spawner_device`
  - `random_item_spawner_device`
- Always check `IsValid()` on the device if you're unsure about its lifetime.
- `ItemPickedUpEvent` is critical for designing collection mechanics (like scoring, unlocking, or quests).

---

## 🧠 Best Practices

| Tip                 | Explanation                                                                                 |
| ------------------- | ------------------------------------------------------------------------------------------- |
| Use Derived Devices | Use `item_spawner_device` instead of this base class unless you're writing custom wrappers. |
| Bind Events         | Subscribing to `ItemPickedUpEvent` is essential for gameplay responses.                     |
| Manage Timing       | Use `Enable()` and `Disable()` wisely to control item spawning windows.                     |
| Animate With Care   | `MoveTo()` will cancel any current animations on the object.                                |

