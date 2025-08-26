# changing\_booth\_device – UEFN Verse Device Documentation

## 🔹 Description

The `changing_booth_device` allows players to change their outfit during gameplay. When a player interacts with the booth, it opens a UI that lets them choose from their locker cosmetics (within Creative rules). This enhances immersive scenarios such as:

- Roleplay games
- Team-based dress codes
- Mid-match disguise mechanics

Players interact with the booth like any other device, and it can be enabled or disabled dynamically through Verse or other devices.

---

## 🧱 Imports Required

```verse
using { /Fortnite.com/Devices }
```

---

## 🔗 Inheritance Hierarchy

| Class                   | Description                                   |
| ----------------------- | --------------------------------------------- |
| `creative_object`       | Base for props and devices.                   |
| `creative_device_base`  | Adds standard device logic.                   |
| `changing_booth_device` | Allows agents to change their outfit in-game. |

---

## ⟳ Main Event

This device does **not** expose listenable events. It is activated through **player interaction** and optionally controlled using **Verse**.

---

## 🧠 Core Methods

| Method Signature                | Description                                     |
| ------------------------------- | ----------------------------------------------- |
| `Enable(): void`                | Enables the booth, allowing player interaction. |
| `Disable(): void`               | Disables the booth so it can’t be used.         |
| `IsEnabled(): logic`            | Returns whether the device is currently active. |
| `GetTransform(): transform`     | Returns the booth’s transform in the world.     |
| `TeleportTo(...) / MoveTo(...)` | Move or reposition the booth dynamically.       |

---

## ⚙️ Configuration Options (Details Panel)

| Option                | Description                                                           |
| --------------------- | --------------------------------------------------------------------- |
| Enabled at Game Start | Determines whether players can use the booth at match start.          |
| Activating Team       | Restrict booth access to specific teams.                              |
| Allowed Class         | Limit use to specific player classes (if using class-based gameplay). |
| Visibility Settings   | Customize booth appearance (optional).                                |
| One-Time Use          | Allow players to use the booth only once per match.                   |

> 👭 Only human agents (players) can interact with the booth. The feature pulls from the player’s available locker cosmetics.

---

## 🚦 Common Usage: Step-by-Step Example

```verse
using { /Fortnite.com/Devices }

booth_control := class(
    @editable OutfitBooth: changing_booth_device
):

    OnBegin<override>() :=
        OutfitBooth.Enable()  # Enable the booth when match starts

    DisableMidGame(): void =
        OutfitBooth.Disable()  # Optionally disable after a certain phase
```

---

## 🧠 Best Practices

- Use in roleplay, story-driven, or team-based islands to encourage identity shifts or uniform requirements.
- Combine with `trigger_device` to enable the booth only in safe zones or lobbies.
- Pair with class selectors to let players choose both class and outfit for immersive roles.
- Use team restriction settings to assign visual uniforms to specific groups.

---

## ❌ Incorrect Usage Examples and How to Fix

| Issue                     | ❌ Wrong                                 | ✅ Fix                                                | Explanation                               |
| ------------------------- | --------------------------------------- | ---------------------------------------------------- | ----------------------------------------- |
| Forgetting to enable      | Expecting booth to be active by default | Call `Enable()` in Verse or enable via Details panel | Must explicitly enable the device         |
| Using on creatures or AI  | AI can't interact with devices          | Booth is for human players only                      | Only human agents are supported           |
| Conflicting classes/teams | All players can change freely           | Use class/team restrictions to control access        | Prevents undesired or unauthorized access |

---

## 🌟 Great For:

- Roleplay maps with different character identities
- Team-based PvP with uniform or disguise mechanics
- Cutscene prep or immersive player transformations
- Lobby areas for visual customization
- Social and sandbox-style experiences

