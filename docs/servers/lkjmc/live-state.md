# lkjmc Live State

## Last Read-Only Check

- Checked at: `2026-06-17T07:50:06Z`
- Method: read-only server-side inspection with non-secret service/config reads
- Public docs updated from this check: yes

## Confirmed Public Entry

- Velocity container was running.
- Minecraft: Java Edition TCP `25565` was published.
- Minecraft: Bedrock Edition UDP `19132` was published.
- Simple Voice Chat UDP `24454` was published.
- Velocity status through the internal server network returned `0/128` players.
- Velocity MOTD advertised Java Edition / Bedrock Edition support, Simple Voice Chat, and `lkjsxc.com`.

## Confirmed Plugins

Velocity had these public-facing plugin categories:

- Geyser and Floodgate for Minecraft: Bedrock Edition access
- Simple Voice Chat for proxy voice routing
- LuckPerms for permissions
- ViaVersion and ViaBackwards for protocol compatibility
- TAB and VelocityScoreboardAPI for tab/scoreboard display
- MiniMOTD for server-list presentation
- oh-my-velocity for join/restart operations
- lkjsxc-plugin for utility commands such as `/hub`

## Confirmed Backend

`lkjmcsmp` was running as the survival backend, with the custom `lkjmcsmp-0.1.0.jar` plugin present.

## Validation Gap

A Java Edition status query from the current development container to the public IP timed out during this pass, while the internal server-network status query succeeded. Treat this as an external-network validation gap, not proof of public outage. If players report reachability problems, verify from a true external network and Discord.
