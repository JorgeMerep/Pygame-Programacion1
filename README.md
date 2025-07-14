# 🐉 Dragon Ball TCG - Juego de Cartas

## 📖 Descripción General

**Dragon Ball TCG** es un juego de cartas basado en el universo de **Dragon Ball**, desarrollado en **Python** con **Pygame**.  
Simula un combate por turnos entre el jugador y un enemigo controlado por la computadora, donde cada carta posee estadísticas únicas de **ataque**, **defensa**, **vida** y **bonificaciones especiales**.

---

## 🎮 Concepto del Juego

### ⚔️ Mecánica Principal

- **Jugador vs Enemigo:** Cada uno tiene un mazo generado aleatoriamente.
- **Revelación de Cartas:** Ambos revelan una carta por turno.
- **Combate:** Las cartas se enfrentan según sus estadísticas de ataque.
- **Daño:** El perdedor recibe daño que afecta sus estadísticas totales.

### 📊 Estadísticas de las Cartas

Cada carta contiene:

- 💖 **HP (Puntos de Vida):** Resistencia de la carta.
- 🗡️ **ATK (Ataque):** Poder ofensivo.
- 🛡️ **DEF (Defensa):** Capacidad defensiva.
- 🎯 **BONUS (%):** Mejora porcentual sobre todas las estadísticas.

---

## ✨ Sistema de Buffs

El jugador puede activar un buff especial **una vez por partida**:

- 🛡️ **Shield:** Refleja el daño recibido al enemigo.
- 💚 **Heal:** Restaura completamente la vida del jugador.

---

## 🏁 Condiciones de Victoria / Derrota

El juego finaliza si se cumple alguna de estas condiciones:

- ⏳ **Tiempo agotado:** El cronómetro llega a 0.
- 📭 **Mazos vacíos:** Ambos jugadores se quedan sin cartas.
- 💔 **HP en 0:** Algún jugador pierde toda su vida.

---

## 🧮 Sistema de Puntuación

- ✅ **+1 punto** por cada mano ganada.
- 📈 El **puntaje total** se acumula al final.
- 🏅 **Ranking permanente** con los mejores puntajes.

---

## 🎯 Mecánicas de Juego

### 🎴 Generación de Mazos

- Los mazos se generan aleatoriamente desde múltiples **expansiones**.
- Cada expansión tiene características propias (verde, azul, rojo, púrpura).
- Las cantidades por expansión varían según el **nivel**.


