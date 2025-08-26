# step2_Code_correct_user_prompt="""
# As a Verse programming expert, your task is to analyze, correct, and refactor the provided code. Your goal is to produce a fully functional and optimized solution.

# ### Methodology to Follow:

# 1.  **Analyze Context:** First, meticulously review the `Device Documentation and Context`. This is your primary source of truth for the specific requirements.
# 2.  **Scrutinize Code:** Compare the `Generated Verse Code to Correct` against the context. Identify not just explicit syntax errors but also logical flaws, anti-patterns, or non-standard practices.
# 3.  **Synthesize and Correct:** This is the most critical step. **Leverage your extensive internal training** on the Verse language and UEFN best practices to create a superior solution. If the provided context is incomplete, **use your own knowledge** to fill in the gaps and ensure the final code is robust, efficient, and production-quality.
# 4.  **Format Output:** Your entire response **MUST** be a single, raw JSON object that strictly conforms to the `CorrectingCodeSolution` schema provided below. Do not include any other text, explanations, or markdown formatting (like ```json) outside of the JSON object itself.

# ---

# ### Generated Verse Code to Correct:
# ```verse
# {{Generated_Verse_Code}}

# Device Documentation and Context:
# {{Device_Context}}

# Required Output Format:
# Your output must be a JSON object matching this Pydantic schema:

# {
#   "prefix": "A brief explanation of the corrections made and the approach taken.",
#   "corrected_imports": "The necessary import statements for the Verse code. If no new imports are needed, specify so. e.g., 'using { /Fortnite.com/Devices }\\nusing { /Verse.org/Simulation }'",
#   "corrected_code": "The main body of the corrected Verse code. This should not include the import statements, which belong in the 'corrected_imports' field."
# }

# Remember: Provide only the final, fully corrected Verse code block as your response in the following format.

# IMPORTANT RULES must Follow while correcting the verse code must follow:
# > Always declare modules using ModuleName := module: syntax in Verse.
# >

# > - Do NOT use module ModuleName: > - Do NOT use module ModuleName { ... }
# > - Always use := for creating a module and follow it with a colon.

# > - Ensure there is a blank line before your module declaration (after imports or other statements).

# Incorrect Example (causes error):
# verse
# module combined_systems:
#     # ... code ...

# verse
# module combined_systems {
#     # ... code ...
# }

# Correct Example (no error):
# verse
# combined_systems := module:
#     # ... code ...

    
# Verse Statement Separation Rule
# > Always separate each top-level statement or declaration in Verse by a newline or semicolon.
# >

# > You must NOT place a variable, function, or class declaration immediately after an expression without a separator.

# >

# > #### Incorrect Example (will cause error):
# > ``verse

# > SomeStatement()

# > combined_systems := class:

# > # class body

# > `

# >

# > #### Correct Example (use a blank line or a semicolon):
# > `verse

# > SomeStatement()

# >

# > combined_systems := class:

# > # class body

# > `

# > *or:*

# > `verse

# > SomeStatement(); combined_systems := class:

# > # class body

# > ``

# >

# > Also, ensure proper indentation and block usage where required.

# > - DO NOT use ToString on enums or custom types in Verse.
# > If you need to print or log an enum value, always define your own mapping function that returns a string for each possible value of the enum.

# >

# > - Example:
# > ``verse

# > MY_ENUM := enum:

# > ValueA

# > ValueB

# >

# > MyEnumToString(Value : MY_ENUM) : string =

# > case(Value):

# > MY_ENUM.ValueA => "ValueA"

# > MY_ENUM.ValueB => "ValueB"

# >

# > # Usage:

# > Print("Current: {MyEnumToString(CurrentState)}")

# > `


# > - Never attempt: Print(SomeEnumValue.ToString()) or ToString(SomeEnumValue)`; this will always cause a build error.
# > - Do NOT change any control flow structures in the code (if, guard, else, block indentation, etc.).

# > - Do NOT convert, remove, or refactor existing code patterns; maintain all current structure and syntax.

# > - Only check and correct device reference names, event subscriptions and handler signatures, and add necessary using { ... } imports if missing.

# > - NEVER remove or reduce any existing using { ... } imports.

# > - Do NOT change core syntax or logic except to annotate or fix device/event/import errors.

# • Automatically define any missing tag classes:
# If code references a tag (e.g., collectable_coins) that is not declared as a class(tag){} in the Verse file, automatically add a declaration for it near the top of the file (typically after the using statements):

# verse
# collectable_coins := class(tag){}

# 1. Wildcard (_) in Closed Enum Case
# *Always remove the _ => ... (wildcard) branch from a case statement on an enum if all possible enum values are already listed. Including a wildcard in this case will cause a warning.*

# Example:
# verse
# # Correct
# case (State):
#     MyEnum.A => ...
#     MyEnum.B => ...
#     MyEnum.C => ...
 
# # Incorrect (will warn)
# case (State):
#     MyEnum.A => ...
#     MyEnum.B => ...
#     MyEnum.C => ...
#     _ => ... # REMOVE this line


# 2. Enum to String Conversion
# *Never use ToString() on enums in Verse. Instead, always implement your own converter function using a case expression covering all enum values.*

# Example:
# verse
# # For enum MyEnum{A,B,C}
# MyEnumToString(State:MyEnum):string =
#     case (State):
#         MyEnum.A => "A"
#         MyEnum.B => "B"
#         MyEnum.C => "C"


# 3. <decides> with Logic Return
# *Never mark a function with <decides> if it returns a logic type (or vice versa). For a function that always returns logic, do not use <decides>. If you need a failable function, use <decides> only with types that can fail (e.g., void or option types).*

# Example (Always returns logic—correct):
# verse
# IsPlayerDead():logic =
#     false

# Example (Failable—correct):
# verse
# IsSomethingTrue()<decides>:void =
#     # Succeeds or fails, does not return logic
#     false?

# follow above things while generating correct code i dont want any syntex errors never ever i want build success code.

# """

# <methodology>
#     <step id="1">**Analyze Context:** Meticulously review the provided `<device_context>`. This is your primary source of truth for the device's specific requirements.</step>
#     <step id="2">**Scrutinize Code:** Compare the `<code_to_correct>` against the context and the `<correction_rules>`. Identify all syntax errors, logical flaws, and deviations from best practices.</step>
#     <step id="3">**Synthesize and Correct:** Rewrite the code to fix all identified issues. Your corrections must strictly follow the rules in this prompt. If context is missing for a standard Verse or Fortnite API call, use your knowledge of the established API, but prioritize the rules in this prompt above all else.</step>
#     <step id="4">**Format Output:** Your entire response MUST be a single, raw JSON object conforming to the `<output_specification>`.</step>
#   </methodology>


step2_Code_correct_user_prompt="""
<verse_correction_prompt>

  <task_definition>
    As a Verse programming expert, your task is to analyze, correct, and refactor the provided code. Your goal is to produce a fully functional and optimized solution that will build successfully in UEFN.
  </task_definition>

  <methodology>
    <step id="1">**Analyze Code Type:** First, determine if the `<code_to_correct>` defines a `class(creative_device)` or a `class(component)`. This determines the primary knowledge source.</step>
    <step id="2">**Prioritize Knowledge Source:**
        <sub_step id="2a">If the code is a **Scene Graph component**, your primary source of truth is the **`<scene_graph_knowledge_base>`**. You must strictly correct all syntax and patterns to match this knowledge base. For any `creative_device` APIs used within the component (like a `volume_device`), you will only validate and correct the event names and subscription arguments based on the `<device_context>`.</sub_step>
        <sub_step id="2b">If the code is a **creative device**, your primary source of truth is the **`<device_context>`**. You will focus on correcting device-specific API calls, event names, and subscription arguments.</sub_step>
    </step>
    <step id="3">**Synthesize and Correct:** Rewrite the code to fix all identified issues. Your corrections **MUST be based exclusively on the provided knowledge bases and `<correction_rules>`**. Do not add, assume, or use any external knowledge or APIs that are not explicitly defined in the provided context.
    </step>
    <step id="4">**Format Output:** Your entire response MUST be a single, raw JSON object conforming to the `<output_specification>`.</step>
  </methodology>

  <input_data>
    <device_context>
      {
{
{{Device_Context}}
}
}
    </device_context>
    <code_to_correct>
      ```verse
      {
{
{{Generated_Verse_Code}}
}
}
      ```
    </code_to_correct>


<scene_graph_knowledge_base>
<!-- ================================================================= -->
<!-- SCENE GRAPH KNOWLEDGE BASE                                          -->
<!-- ================================================================= -->
<section id="SCENE_GRAPH_KNOWLEDGE_BASE">
  
  <subsection id="CONCEPTS">
    | Term | Type | Description |
    |---|---|---|
    | `entity` | Object | The fundamental container in Scene Graph. Has a transform but no inherent behavior or visuals. Can be nested in hierarchies. |
    | `component` | Class | A reusable piece of functionality (a "brain" or "skill") that is attached to an `entity` to give it behavior. |
    | `prefab` | Asset | A pre-configured collection of entities and components saved as a single asset that can be instantiated. |
  </subsection>

  <subsection id="CORE_SYNTAX_PATTERNS">
    <pattern name="Component Uniqueness Rule">
      <description>An entity can only have ONE component of a given subclass at a time. You cannot add two `point_light_component`s to the same entity.</description>
    </pattern>
    <pattern name="Adding a Component in Verse">
      <description>To add a component at runtime, you must first create an instance of it and then pass it to `Entity.AddComponents()` inside an array.</description>
      <correct_example>
        ```verse
        NewComponent := my_component_type{}
        Entity.AddComponents(array{NewComponent})
        ```
      </correct_example>
    </pattern>

  </subsection>

  <!-- UPDATED: Added keyframed_movement_component to the table -->

  <subsection id="BUILTIN_COMPONENTS_REFERENCE">
    | Component | Key Event / Method | Signature / Type | Description |
    |---|---|---|---|
    | `mesh_component` | `EntityEnteredEvent` | `listenable(entity)` | Fires when another entity's collision overlaps this mesh. |
    | `interactable_component` | `SucceededEvent` | `listenable(agent)` | Fires when a player successfully completes an interaction. |
    | `keyframed_movement_component` | `Play() / Stop() / Pause()` | `void` | Controls the playback of a keyframed animation. |
    | `light_component` | `Enable() / Disable()` | `void` | Turns the light source on or off. |
    | `particle_system_component` | `Play() / Stop()` | `void` | Controls the playback of a particle effect. |
  </subsection>

  <subsection id="KEYFRAMED_MOVEMENT_COMPONENT_DETAILS">
    <description>
      The `keyframed_movement_component` animates an entity by moving it smoothly between a series of keyframes. It is the primary tool for creating animations in Verse Scene Graph.
      - Required Import: `using { /Verse.org/SceneGraph/KeyframedMovement }`
      - Note: Transform values use the FRU (Forward, Right, Up) coordinate system.
    </description>
    
    <api_details>
      | Method | Signature | Description |
      |---|---|---|
      | `SetKeyframes` | `SetKeyframes(Keyframes:[]keyframed_movement_delta, Mode:keyframed_movement_playback_mode)` | Sets the animation sequence and playback mode. |
      | `Play` | `Play()` | Starts playing the currently set animation. |
      | `Stop` | `Stop()` | Stops the animation completely. |
      | `Pause` | `Pause()` | Pauses the animation at its current state. |
    </api_details>

    <data_types>
      | Data Type | Description |
      |---|---|
      | `keyframed_movement_delta` | A single keyframe in an animation, containing a `Transform`, `Duration`, and `Easing`. |
      | `movement_mode` | An enum to define the animation's behavior after completion. |
    </data_types>

    <enum_values name="movement_mode">
      | Value | Description | Corresponding Playback Mode |
      |---|---|---|
      | `OneShot` | Plays the animation once and stops. | `oneshot_keyframed_movement_playback_mode{}` |
      | `Loop` | Restarts the animation from the beginning when it finishes. | `loop_keyframed_movement_playback_mode{}` |
      | `PingPong` | Plays the animation forward, then in reverse, continuously. | `pingpong_keyframed_movement_playback_mode{}` |
    </enum_values>

    <correct_example title="Full Component Example: Simple Movement">
      ```verse
      using { /Verse.org }
      using { /Verse.org/Native }
      using { /Verse.org/SceneGraph }
      using { /Verse.org/Simulation }
      using { /Verse.org/SceneGraph/KeyframedMovement }

      movement_mode<public> := enum:
          OneShot
          Loop
          PingPong

      simple_movement_component<public> := class<final_super>(component):

          @editable
          var Keyframes: []keyframed_movement_delta = array{}

          @editable
          var AutoPlay: logic = true

          @editable
          MovementMode: movement_mode = movement_mode.Loop
              
          OnSimulate<override>()<suspends>:void =
              Sleep (0.1)
              if:
                  KeyframedMovementComponent := Entity.GetComponent[keyframed_movement_component]
              then:
                  InitializeKeyframedMovementComponent(KeyframedMovementComponent)
              else:
                  NewKeyFramedMovementComponent := keyframed_movement_component { Entity := Entity }
                  Entity.AddComponents(array{ NewKeyFramedMovementComponent })
                  InitializeKeyframedMovementComponent(NewKeyFramedMovementComponent)

          InitializeKeyframedMovementComponent(InKeyframedMovementComponent:keyframed_movement_component):void =
              var PlaybackMode:keyframed_movement_playback_mode = oneshot_keyframed_movement_playback_mode{}
              
              case (MovementMode):
                  movement_mode.OneShot =>
                      set PlaybackMode = oneshot_keyframed_movement_playback_mode{}
                  movement_mode.Loop =>
                      set PlaybackMode =  loop_keyframed_movement_playback_mode{}
                  movement_mode.PingPong =>
                      set PlaybackMode = pingpong_keyframed_movement_playback_mode{}

              InKeyframedMovementComponent.SetKeyframes(Keyframes, PlaybackMode) 
              
              if:
                  AutoPlay?
              then:
                  InKeyframedMovementComponent.Play()
      ```
    </correct_example>
  </subsection>

  <subsection id="INTERACTABLE_COMPONENTS_DETAILS">
    <description>
      Interactable components are Scene Graph components designed to simplify basic player interactions in UEFN. These components enable agents to interact with the entity that the components are attached to. Interaction is defined by the agent attempting to start, and being signaled on, the success of the interaction — for instance, pressing the E key on PC. The component doesn’t dictate what an interaction does, but only handles the handshake between the interacting agent and the interactable component. The interactable_component needs to be attached to a mesh_component to work.
    </description>

    <api_definition title="interactable_component">
      <description>The basis for granting players the ability to interact with objects in a game. It can start an interaction and manage cooldowns for both the component and for each agent that interacts with it.</description>
      ```verse
      # An interactable component allows an agent to start and succeed at an interaction.
      # The functionality of what happens on success should be implemented by overriding the success event.
      interactable_component<public> := class(component, enableable):
          # Set the enable/disable for interaction of the component.
          Enable<override>()<transacts> : void
          Disable<override>()<transacts> : void
          IsEnabled<override>()<decides><reads> : void
      
          # Event fires when an interaction starts. Sends the interacting agent.
          StartedEvent<public> : listenable(agent) = external{}
      
          # Event fires when an interaction has completed successfully. Sends the formerly interacting agent.
          SucceededEvent<public> : listenable(agent) = external{}
      
          # Event fires when an interaction has ended before completing successfully. Sends the formerly interacting agent.
          # This event is called on all interacting agents when Disable() is called on the component.
          CanceledEvent<public> : listenable(agent) = external{}
      
          # Fires the StartedEvent event.
          SignalStartEvent<protected>(:agent)<transacts> : void
      
          # Fires the SucceededEvent event.
          SignalSucceedEvent<protected>(:agent)<transacts> : void
      
          # Fires the CanceledEvent event.
          SignalCancelEvent<protected>(:agent)<transacts> : void
      
          # Attempt to start an interaction. Fails if the agent does not pass the CanInteract function.
          Start<public><final>(:agent)<decides><transacts> : void
          
          # Called from Start if CanInteract passes successfully to start the interaction. Overriding this function will allow you to create a custom interaction behaviour.
          OnStart<protected>(:agent)<decides><transacts> : void
      
          # Returns whether the specified agent can interact.
          CanInteract<public>(:agent)<decides><reads> : void
      
          # Returns an appropriate message to display to players to communicate the current state of the interactable.
          InteractMessage<public>(:agent)<decides><reads> : message
      ```
    </api_definition>

    <api_definition title="basic_interactable_component">
        <description>An interactable component with a composable feature set. It allows for interactions to have a duration that must elapse before the interaction succeeds, and it handles the complexity around this by potentially allowing multiple interactions simultaneously. It also allows a way to manage the cooldown time between each interaction.</description>
        ```verse
        # An interactable component with a composable feature set.
        basic_interactable_component<public> := class(interactable_component):
            # Cooldowns begin elapsing on successful interactions. A cooldown which applies for all attempts to interact on this component.
            @editable
            Cooldown<public> : ?interactable_cooldown = false
        
            # Cooldowns begin elapsing on successful interactions. A cooldown which applies for future attempts to interact on this component by the agent which succeeded.
            @editable
            CooldownPerAgent<public> : ?interactable_cooldown_per_agent = false
        
            # Success limits prevent new interactions once the component has been successfully interacted with a specified number of times.
            @editable
            SuccessLimit<public> : ?interactable_success_limit = false
        
            # An interaction with a duration does not succeed until the duration has elapsed, and success is not guaranteed as it can be canceled while the duration is active.
            @editable
            InteractableDuration<public> : ?interactable_duration = false
        
            # The agents which are currently interacting with this interactable.
            var<private> InteractingAgents<public> : []agent
        
            # Attempt to cancel an interaction. Fails if the supplied agent is not currently interacting with the component.
            Cancel<public>(:agent)<decides><transacts> : void
        
            # Attempt to succeed at an interaction.
            # Success will also happen automatically after InteractDuration has elapsed after starting an interaction, provided that interaction wasn’t ended before then.
            # Fails if the agent is not currently interacting with the component.
            Succeed<public>(:agent)<decides><transacts> : void
        
            # Get the remaining cooldown of the interactable for the supplied agent.
            # This returns the duration left in seconds of either the shared or per agent cooldown, whichever is greater.
            # Returns the same value when called multiple times within a transaction.
            GetRemainingCooldownDurationAffectingAgent<public>(:agent)<reads> : float
        ```
    </api_definition>

    <correct_example title="Example 1: Toggling an Enabled/Disabled State">
      ```verse
      using { /Verse.org }
      using { /Verse.org/SceneGraph }
      using { /Verse.org/Simulation }
      using { /[Fortnite.com/Game](https://Fortnite.com/Game) }
      
      # Allows a Enable/Disable state on the interactable_component
      interactable_enableable_component<public> := class<final_super>(interactable_component):
      
          # Default text to show on the UI
          EnabledText<localizes> : message = "Enabled"
          DisabledText<localizes> : message = "Disabled"
      
          # Handles to cancel the subscriptions
          var RoundStartedHandle<public>:?cancelable = false
          var RoundEndedHandle<public>:?cancelable = false
          var SucceededEventHandle<public>:?cancelable = false
      
          # Stores the state of the interaction
          var IsInteractEnabled<protected>:logic = true
      
          OnBeginSimulation<override>():void =
              # Run OnBeginSimulation from the parent class before
              # running this component's OnBeginSimulation logic
              (super:)OnBeginSimulation()
      
              # Subscribes to round start/end 
              if (RoundManager := Entity.GetFortRoundManager[]):
                  RoundStartedCancelable := RoundManager.SubscribeRoundStarted(OnBeginRound)
                  set RoundStartedHandle = option{RoundStartedCancelable}
      
                  RoundEndedCancelable := RoundManager.SubscribeRoundEnded(OnEndRound)
                  set RoundEndedHandle = option{RoundEndedCancelable}
      
          OnEndSimulation<override>():void =
              # Run OnEndSimulation from the parent class before
              # running this component's OnEndSimulation logic
              (super:)OnEndSimulation()
      
              # Cancel round start/end
              if (RoundStartedCancelable := RoundStartedHandle?):
                  RoundStartedCancelable.Cancel()
      
              if (RoundEndedCancelable := RoundEndedHandle?):
                  RoundEndedCancelable.Cancel()
      
          OnBeginRound<protected>():void=
              Print("Round Started!")
              set SucceededEventHandle = option{SucceededEvent.Subscribe(OnSucceed)}
      
          OnEndRound<protected>():void=
              Print("Round Ended!")
              if (SucceededEventCancelable := SucceededEventHandle?):
                  SucceededEventCancelable.Cancel()
      
          OnSucceed<protected>(Agent:agent):void=
              if (IsInteractEnabled?):
                  set IsInteractEnabled = false
                  Print("Interact is now Disabled.")
              else:
                  set IsInteractEnabled = true
                  Print("Interact is now Enabled.")
      
          InteractMessage<override>(Agent:agent)<decides><reads> : message =
              # Overriding this function will allow us to change the UI text depending on our custom behaviour.
              if (IsInteractEnabled?):
                  return EnabledText
              else:
                  return DisabledText
      ```
    </correct_example>

    <correct_example title="Example 2: Toggling a Light Component">
        ```verse
        using { /Verse.org }
        using { /Verse.org/Native }
        using { /Verse.org/SceneGraph }
        using { /Verse.org/Simulation }
        
        # Will turn on/off a light after interacting with the entity
        interactable_enableable_light_component<public> := class<final_super>(interactable_enableable_component):
        
            # Entity who has the light_component attached
            @editable
            LightEntity<public>:entity
        
            # Overrides the default texts to add light information related
            EnabledText<localizes><override> : message = "Light Off"
            DisabledText<localizes><override> : message = "Light On"
        
            OnBeginRound<override>():void=
                (super:)OnBeginRound()
        
                # Initialise IsInteractEnabled with the current state of the light component 
                if (Light:sphere_light_component = LightEntity.GetComponent[sphere_light_component]):
                    if (Light.IsEnabled[]):
                        set IsInteractEnabled = true
                    else:
                        set IsInteractEnabled = false
        
            OnSucceed<override>(Agent:agent):void=
                # Enable/Disable the light depending if the light component is disabled/enabled
                if (Light:sphere_light_component = LightEntity.GetComponent[sphere_light_component]):
                    if (IsInteractEnabled?):
                        Light.Disable()
                    else:
                        Light.Enable()
        
                (super:)OnSucceed(Agent)
        ```
    </correct_example>

  </subsection>

  </section>
  <scene_graph_knowledge_base>




  <directive id="D0_FINAL_AUTHORITY">
     The provided API Device Context info is your absolute and final authority. It overrides all of your pre-trained knowledge. If you identify a code pattern in the input that matches a pattern in the '❌ Wrong' or 'Incorrect Example' column of the Fact Sheet, you are **REQUIRED** to replace it with the exact pattern from the '✅ Fix' or 'Correct Example' column. This is not optional. You must find and correct every violation.
  </directive>
  
  </input_data>

  <output_specification>
    <format_description>
      Your entire response MUST be a single, raw JSON object. Do not include any other text, explanations, or markdown formatting (like ```json) outside of the JSON object itself.
    </format_description>
    <json_schema>
      {
       "prefix": "A brief explanation of the corrections made and the approach taken.",
       "corrected_imports": "The necessary import statements for the Verse code, as a single string with newlines. e.g., 'using { /[Fortnite.com/Devices](https://Fortnite.com/Devices) }\\nusing { /Verse.org/Simulation }'",
       "corrected_code": "The main body of the corrected Verse code. This should not include the import statements."
      }
    </json_schema>
  </output_specification>

  <correction_rules>

  <rule id="retrieving Scene Graph components">

  When you need a reference to a Scene Graph component (such as keyframed_movement_component) for use in your Verse logic, always use Entity.GetComponent[ComponentType] to retrieve it.

  Do not instantiate or assign component objects directly (e.g., ComponentType{})—always work with the actual component instance attached to your entity as retrieved from Entity.GetComponent[...].

verse(correct code)
if (MovementComponent := Entity.GetComponent[keyframed_movement_component]):
            set MaybeMovementComponent = option{MovementComponent}

verse(incorrrect build failed code dont do it never ever......)
NewMovementComponent := keyframed_movement_component{}
        set MaybeMovementComponent = option{NewMovementComponent}  # This is NOT the attached instance!
incorrect code :
# Get or create the movement component if it doesn't exist
        if (ExistingMovementComponent := Entity.GetComponent[keyframed_movement_component]):
            set MovementComponent = option{ExistingMovementComponent}
        else:
            if(NewMovementComponent := Entity.AddComponents(array{keyframed_movement_component{}})[0]):
                set MovementComponent = option{NewMovementComponent}
correct code:
if (ExistingMovementComponent := Entity.GetComponent[keyframed_movement_component]):
            set MovementComponent = option{ExistingMovementComponent}
dont include else here in this type of logic we will consider we always have a entity and component present so if will success okk
**This rule ensures your code is robust and that you always interact with the real, entity-attached component instance in Unreal Editor for Fortnite (UEFN) Scene Graph.
  </rule>

    <rule id="R0_LOGIC_IF_SYNTAX">
        <description>
            When checking a value of type `logic` (Verse's boolean) in an `if` or similar failure context, you must use the *failable* query operator `?`, e.g., `if(IsAnimating?):`. The plain form `if(IsAnimating):` is NOT valid Verse syntax and will cause build errors. Only correct the use of logic variable checks; do not alter program flow.
        </description>
        <incorrect_example title="Using logic variable without query operator (Wrong)">
            ```verse
            if(IsAnimating): # ERROR: Not valid in Verse!
                return
            ```
        </incorrect_example>
        <correct_example title="Using logic variable with query operator (Correct)">
            ```verse
            if(IsAnimating?): # CORRECT: Only executes if IsAnimating is true
                return
            ```
        </correct_example>
    </rule>



    <rule id="R1_SCOPE_OF_CHANGES">
      Your primary goal is correction to ensure the code builds successfully. You must maintain the original code's core logic and control flow structures (if, for, guard, etc.). Do not perform major refactoring unless it is necessary to fix a build error as defined by another rule. You must not remove any existing `using` imports.
    </rule>
     
    <rule id="R2_MODULE_SYNTAX">
      <description>You must declare all modules using the `ModuleName := module:` syntax. Ensure there is a blank line before the module declaration.</description>
      <incorrect_example>
        ```verse
        module combined_systems:
        # ... code ...

        module combined_systems {
          # ... code ...
        }
        ```
      </incorrect_example>
      <correct_example>
        ```verse
        combined_systems := module:
          # ... code ...
        ```
      </correct_example>
    </rule>
     
    <rule id="R3_STATEMENT_SEPARATION">
      <description>You must ensure every top-level statement or declaration is separated by a newline.</description>
      <incorrect_example>
        ```verse
        SomeStatement()
        combined_systems := class:
          # class body
        ```
      </incorrect_example>
      <correct_example>
        ```verse
        SomeStatement()

        combined_systems := class:
          # class body
        ```
      </correct_example>
    </rule>

    <rule id="R4_ENUM_TO_STRING">
      <description>You must NEVER use `.ToString()` on enums. If string conversion is required, you must implement a custom converter function using a `case` expression that explicitly handles every enum value.</description>
      <correct_example>
        ```verse
        MY_ENUM := enum:
          ValueA
          ValueB

        MyEnumToString(Value : MY_ENUM) : string =
          case(Value):
            MY_ENUM.ValueA => "ValueA"
            MY_ENUM.ValueB => "ValueB"

        # Usage:
        Print("Current: {MyEnumToString(CurrentState)}")
        ```
      </correct_example>
    </rule>

    <rule id="R5_TAG_CLASS_DEFINITION">
      <description>If the code references a custom tag that is not declared, you must automatically add its class definition at the top of the file after the imports.</description>
      <correct_example>
         ```verse
         collectable_coins := class(tag){}
         ```
      </correct_example>
    </rule>

    <rule id="R6_WILDCARD_IN_ENUM_CASE">
      <description>You must remove the wildcard `_ => ...` branch from a `case` statement on an enum if all possible enum values are already explicitly handled.</description>
      <incorrect_example>
        ```verse
        case (State):
          MyEnum.A => ...
          MyEnum.B => ...
          MyEnum.C => ...
          _ => ... # REMOVE this line
        ```
      </incorrect_example>
      <correct_example>
        ```verse
        case (State):
          MyEnum.A => ...
          MyEnum.B => ...
          MyEnum.C => ...
        ```
      </correct_example>
    </rule>
     
    <rule id="R7_DECIDES_FUNCTION_RETURN">
      <description>You must ensure that a function marked with `<decides>` does NOT have a `logic` return type.</description>
      <correct_example title="Failable Function (Correct)">
         ```verse
         IsSomethingTrue()<decides>:void =
          # Succeeds or fails, does not return logic
          false?
         ```
      </correct_example>
      <correct_example title="Logic-Returning Function (Correct)">
         ```verse
         IsPlayerDead():logic =
          false
         ```
      </correct_example>
    </rule>

    <rule id="R8_SUSPENDS_CONTEXT">
    <description>You must not call an asynchronous operation (like `spawn`, `Sleep`, or `Await`) from a synchronous function (a function without the `<suspends>` specifier). Many device event handlers, such as `SpawnedEvent` or `InteractedWithEvent`, are synchronous. If an asynchronous operation is required, you MUST refactor the code to use a "Suspending Wrapper" pattern where the synchronous handler calls a new, separate function that is correctly marked with `<suspends>`.</description>
    <incorrect_example title="Spawning from a Synchronous Function (Wrong)">
        ```verse
        # This will cause a build error because OnPlayerSpawned does not have <suspends>.
        OnPlayerSpawned(Agent : agent): void=
            spawn{GiveItem(Agent)} # ERROR: Cannot spawn from a non-suspending function.

        GiveItem(Agent : agent)<suspends>:void=
            Sleep(1.0)
            ItemGranter.GrantItem(Agent)
        ```
    </incorrect_example>
    <correct_example title="Using a Suspending Wrapper (Correct)">
        ```verse
        # The event handler is synchronous, but it is allowed to spawn a new function.
        OnPlayerSpawned(Agent : agent): void=
            spawn{OnPlayerSpawned_Async(Agent)}

        # This new wrapper function IS marked with <suspends>.
        OnPlayerSpawned_Async(Agent : agent)<suspends>:void=
            # Now it is safe to call other suspending functions from here.
            GiveItem(Agent)

        GiveItem(Agent : agent)<suspends>:void=
            Sleep(1.0)
            ItemGranter.GrantItem(Agent)
        ```
    </correct_example>
    </rule>
  </correction_rules>

</verse_correction_prompt>
"""