📘 **timed\_objective\_device – UEFN Verse Device Documentation**

---

🔹 **Description**

The `timed_objective_device` configures game modes where players can start, pause, resume, or stop timers to advance gameplay objectives—such as Attack/Defend Bomb, control point, or speedrun scenarios. The device features HUD countdowns, customizable labels, per-team interaction options, scoring, and event signaling for each phase of the objective.

---

🧱 **Verse Using Statement**

```verse
using { /Fortnite.com/Devices }
```

---

🔗 **Inheritance Hierarchy**

- creative\_object
- creative\_device\_base
- timed\_objective\_device

---

🛠️ **Main Functions & Methods**

| Name                       | Description                                                                |
| -------------------------- | -------------------------------------------------------------------------- |
| Enable(agent) / Enable()   | Enables the objective for one agent or for all.                            |
| Disable(agent) / Disable() | Disables the objective for one agent or for all.                           |
| Show() / Hide()            | Controls device visibility in-game.                                        |
| Begin(agent)               | Starts the objective timer, setting the agent as the activator.            |
| End(agent)                 | Ends/stops the objective timer, setting the agent as the activator.        |
| Pause(agent)               | Pauses the objective timer for agent.                                      |
| Resume(agent)              | Resumes the objective timer for agent.                                     |
| Restart(agent)             | Restarts the timer (back to base value) for agent.                         |
| Complete(agent)            | Completes the timer (marks objective as complete) for agent.               |
| SetMaxDuration(float)      | Changes the countdown time (seconds).                                      |
| GetMaxDuration()           | Gets max allowed duration (float, seconds).                                |
| IsStatePerAgent()          | Returns true if objective state is tracked per agent rather than globally. |

---

🧩 **Events (Data Members)**

| Event Name     | Type              | Description                                              |
| -------------- | ----------------- | -------------------------------------------------------- |
| BeganEvent     | listenable(agent) | Fires when timer is started (who started it).            |
| EndedEvent     | listenable(agent) | Fires when timer is ended/stopped.                       |
| PausedEvent    | listenable(agent) | Fires when timer is paused.                              |
| ResumedEvent   | listenable(agent) | Fires when timer resumes from pause.                     |
| RestartedEvent | listenable(agent) | Fires when timer is restarted (goes back to full value). |
| CompletedEvent | listenable(agent) | Fires on success—timer completion, full progress, etc.   |

---

🎛 **Configuration Options (Details Panel)**

| Option                         | Description                                                     |
| ------------------------------ | --------------------------------------------------------------- |
| Time                           | Total time for objective (seconds).                             |
| Start/Stop/Complete Score      | Award score for each event.                                     |
| Start/Stop/Restart Team Filter | Which teams can interact at each phase.                         |
| Custom Prompts/Text            | Text for start/stop/restart/pause/resume.                       |
| Label & HUD                    | Label timer on HUD, set style and visibility.                   |
| Hologram Until Activated       | Shows as hologram until interactive.                            |
| Urgency Mode                   | Enable special FX as time nears 0.                              |
| Urgency Start Time             | When urgency FX begin.                                          |
| Completion Behavior            | (Disable, Reset, Restart objective on completion).              |
| *(many more)*                  | Explore editor for all options (team/score/class/fx/broadcast). |

---

🧰 **Verse Usage Example**

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

timed_objective_example := class(creative_device):

    @editable
    Objective : timed_objective_device = timed_objective_device{}

    @editable
    StartButton : button_device = button_device{}
    @editable
    PauseButton : button_device = button_device{}
    @editable
    ResumeButton : button_device = button_device{}
    @editable
    RestartButton : button_device = button_device{}
    @editable
    CompleteButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        # Subscribe to objective events
        Objective.BeganEvent.Subscribe(OnBegan)
        Objective.EndedEvent.Subscribe(OnEnded)
        Objective.PausedEvent.Subscribe(OnPaused)
        Objective.ResumedEvent.Subscribe(OnResumed)
        Objective.RestartedEvent.Subscribe(OnRestarted)
        Objective.CompletedEvent.Subscribe(OnCompleted)

        # Subscribe to control buttons
        StartButton.InteractedWithEvent.Subscribe(OnStart)
        PauseButton.InteractedWithEvent.Subscribe(OnPause)
        ResumeButton.InteractedWithEvent.Subscribe(OnResume)
        RestartButton.InteractedWithEvent.Subscribe(OnRestart)
        CompleteButton.InteractedWithEvent.Subscribe(OnComplete)

    # Event handlers
    OnBegan(Agent : agent) : void =
        Print("Objective started by agent")

    OnEnded(Agent : agent) : void =
        Print("Objective ended by agent")

    OnPaused(Agent : agent) : void =
        Print("Objective paused by agent")

    OnResumed(Agent : agent) : void =
        Print("Objective resumed by agent")

    OnRestarted(Agent : agent) : void =
        Print("Objective restarted by agent")

    OnCompleted(Agent : agent) : void =
        Print("Objective completed by agent")

    # Button control handlers
    OnStart(Agent : agent) : void =
        Objective.Begin(Agent)
        Print("Objective started")

    OnPause(Agent : agent) : void =
        Objective.Pause(Agent)
        Print("Objective paused")

    OnResume(Agent : agent) : void =
        Objective.Resume(Agent)
        Print("Objective resumed")

    OnRestart(Agent : agent) : void =
        Objective.Restart(Agent)
        Print("Objective restarted")

    OnComplete(Agent : agent) : void =
        Objective.Complete(Agent)
        Print("Objective completed")
```

---

📝 **How to Use in UEFN**

**1. Place Devices**

- Place a `timed_objective_device` into your world.
- Add `button_devices` for each control you want (start, stop, pause, etc.).

**2. Configure Options**

- In Details, set timer, score, teams allowed, labels/prompts, urgency mode, etc.

**3. Create and Assign Your Verse Device**

- In *Verse Explorer*, right-click a folder → Create New Verse File (e.g., `timed_objective_example.verse`).
- Create Empty, paste the sample code above, and save.
- Build your Verse file (Verse → Build Verse Code or Ctrl+Shift+B).
- In Content Browser, drag your device into the world and assign all references (Objective, buttons).

**4. Test**

- Play the level and interact with the buttons to test all objective phases and ensure events/logs fire.

---

🧠 **Tips**

- Combine this device with `end_game_device`, timers, sentries, map indicators, or score managers for complex objectives.
- Use Verse events for extra feedback, spawning, or unlocking further objectives when `Complete` or `End` fires.
- Use per-agent state for PvP or asynchronous player objectives.

---

❌ **Common Issues & Solutions**

| Issue                      | Possible Reason                       | Solution                             |
| -------------------------- | ------------------------------------- | ------------------------------------ |
| Buttons do nothing         | Device disabled or references not set | Enable device and set all references |
| Events don’t fire in log   | Not subscribed in Verse code          | Subscribe to all event fields        |
| Wrong teams can use device | Team filters not set                  | Set allowed teams for each action    |

---

📌 **Note:**

- This device is essential for bomb defusal, timed control points, checkpoint races, and speedruns.
- Completion behavior (disable, reset, restart) determines if the objective is one-time or renewable in your game loop.
- For round-based games, combine with `round_settings_device`, `score_manager_device`, and UI feedback for robust control.

