# round\_settings\_device – UEFN Verse Device Documentation

## 🔹 Description

The `round_settings_device` is used to customize gameplay for round-based games in Fortnite. It determines what happens to each agent’s inventory, resources, and rewards at the start and end of rounds. This device can override My Island game settings for item/resource retention, building materials and gold distribution, weapon/restock policies, last player standing rules, respawn/class adjustment, and winner logic. Events and functions allow granular control and round progression via Verse.

## 🛠️ Verse Using Statement

```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy

- creative\_object
- creative\_device\_base
- round\_settings\_device

## 🧹 Events (Data Members)

| Name            | Type         | Description                      |
| --------------- | ------------ | -------------------------------- |
| RoundBeginEvent | listenable() | Fires at the start of each round |

## 🛠️ Functions & Methods

| Name                        | Description                                                        |
| --------------------------- | ------------------------------------------------------------------ |
| Enable()                    | Turns on the device                                                |
| Disable()                   | Turns off the device                                               |
| EnableMatchmaking()         | Allows matchmaking into the island (if set in Island Settings)     |
| DisableMatchmaking()        | Prevents matchmaking into the island                               |
| ToggleMatchmaking()         | Toggles matchmaking on/off                                         |
| DisableEndRoundConditions() | Turns off automatic end-of-round; must end round manually/scripted |
| EndRound(agent)             | Instantly ends the round, marking the agent’s team as the winner   |

## 🎛 Configuration Options (Details Panel)

| Option                    | Description                                                         |
| ------------------------- | ------------------------------------------------------------------- |
| Round                     | Which round(s) this device customizes (All, 1–100)                  |
| Override Keep Items       | Overrides whether players keep items between rounds                 |
| Keep Items Between Rounds | If items should be kept when set to Override                        |
| Reset Class Each Round    | If Yes, resets the player’s class at round start                    |
| Resources Given Per Round | Number of wood, stone, metal, or gold allocated each round          |
| Keep Resources %          | Percentage of resources kept between rounds                         |
| Override Last Standing    | Control win rules for last player standing per round                |
| Reload & Restock Weapons  | Reloads/restocks between rounds (and re-equip/reload after respawn) |
| Respawn on Class Reset    | If players are forced to respawn when class resets                  |
| Clear All Items on Reset  | Wipes player inventory when resetting class                         |
| Reset Current Vitals      | Resets player health/shields on reset                               |
| Enable at Game Start      | If device is enabled as soon as a minigame begins                   |
|                           |                                                                     |

| *(More options in Details)* | Full range—see device for further customizable round settings |
| --------------------------- | ------------------------------------------------------------- |

## 🛠️ Events

| Event           | When It Fires         |
| --------------- | --------------------- |
| RoundBeginEvent | When the round begins |

## 🛠️ Verse Usage Example

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Example device showing how to use round_settings_device
round_settings_example := class(creative_device):

    @editable
    RoundSettings : round_settings_device = round_settings_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    ToggleMatchmakingButton : button_device = button_device{}

    var MatchmakingEnabled : logic = false

    OnBegin<override>()<suspends> : void =
        # Subscribe to round events
        RoundSettings.RoundBeginEvent.Subscribe(OnRoundBegin)

        # Subscribe to control buttons
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        ToggleMatchmakingButton.InteractedWithEvent.Subscribe(OnToggleMatchmaking)

    # Event handlers
    OnRoundBegin() : void =
        Print("Round has begun!")

    # Button control handlers
    OnEnablePressed(Agent : agent) : void =
        RoundSettings.Enable()
        Print("Round settings enabled!")

    OnDisablePressed(Agent : agent) : void =
        RoundSettings.Disable()
        Print("Round settings disabled!")

    OnToggleMatchmaking(Agent : agent) : void =
        if (MatchmakingEnabled?):
            set MatchmakingEnabled = false
            Print("Matchmaking disabled!")
        else:
            set MatchmakingEnabled = true
            Print("Matchmaking enabled!")

    # Example function to end round with agent's team
    EndRoundWithAgentTeam(Agent : agent) : void =
        if (Team := GetPlayspace().GetTeamCollection().GetTeam[Agent]):
            Print("Ending round with agent's team!")
            # Add your round ending logic here
```

### Explanation:

- Reference one `round_settings_device` and three `button_devices` to control enabling, disabling, and matchmaking.
- Listen (Subscribe) for `RoundBeginEvent` to act at the start of each round.
- Allow in-game buttons to toggle core device features dynamically.
- You can call `EndRound(agent)` in Verse to end the round and mark the agent’s team as the winner.

## 📅 How to Use in UEFN

1. **Place Round Settings Device(s)**

   - Drag one or more `round_settings_device` objects into your map (one for All/each round as needed).
   - Configure options in Details panel (round number, inventory/resource handling, rewards, win rules, etc.).

2. **(Optional) Add In-Game Control Buttons**

   - Place three `button_devices` for enable, disable, and toggle matchmaking controls.

3. **Create and Build a Verse Device**

   - In Verse Explorer, right-click a folder → Create New Verse File (e.g., `round_settings_example.verse`).
   - Create Empty, paste the above Verse example code, and save it.
   - Click Verse → Build Verse Code (Ctrl+Shift+B) and verify “Build Succeeded”.

4. **Assign Device References in Details**

   - Place your Verse device into the map.
   - Assign `RoundSettings`, `EnableButton`, `DisableButton`, and `ToggleMatchmakingButton` fields in Details.

5. **Play and Test**

   - Use control buttons to enable/disable/toggle matchmaking.
   - Observe logs, player inventory/resource changes, class resets, and rewards as configured per round.

## 🧠 Best Practices

- Use separate `round_settings_device` objects for each round to customize round-specific rules and rewards.
- Use `DisableEndRoundConditions()` for advanced scripted round endings.
- Use `RoundBeginEvent` to automate logic: scores, spawns, rewards, custom announcements.

## ❌ Common Issues & Solutions

| Issue                       | Problem (❌)                    | Solution (✅)                                                   |
| --------------------------- | ------------------------------ | -------------------------------------------------------------- |
| Device doesn’t affect round | Not enabled, or round mismatch | Enable device/set correct "Round" option                       |
| Matchmaking stuck           | Not toggled via Verse/UI       | Use `.EnableMatchmaking()` / `.DisableMatchmaking()` as needed |
| Options not applied         | Device not properly configured | Adjust in Details and double-check all settings                |

## 🔹 Note

- This device is essential for round-based game modes (e.g., Search and Destroy, round-based deathmatch, tournaments).
- All runtime logic (matchmaking, round end, etc.) should be handled through configured buttons or scripted calls in Verse for full flexibility.

