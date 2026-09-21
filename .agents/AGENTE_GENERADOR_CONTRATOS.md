# 🤖 Agente IA 2: Generador de Contratos & Gestión Legal de Reservas
**Proyecto:** Espacio Mañío — Talagante  
**Objetivo:** Automatizar la redacción, cálculo de saldos y emisión del contrato de arriendo temporal en base a los comprobantes de transferencia.

---

## 📄 1. Entrada de Datos Requerida (Input)
El agente toma de la conversación de WhatsApp los siguientes campos:
1. `NOMBRE_CLIENTE`: Nombre completo del arrendatario.
2. `RUT_CLIENTE`: Cédula de identidad.
3. `TELEFONO_CLIENTE`: WhatsApp de contacto.
4. `FECHA_EVENTO`: Día agendado (DD/MM/AAAA).
5. `NUMERO_PERSONAS`: Capacidad pactada.
6. `VALOR_TOTAL`: Tarifa acordada en pesos chilenos ($).
7. `FECHA_SENA`: Día del pago de la seña.

---

## ⚙️ 2. Lógica de Cálculo Automático
* `MONTO_SENA` = `VALOR_TOTAL * 0.50`
* `SALDO_PENDIENTE` = `VALOR_TOTAL - MONTO_SENA` (se cobra al ingreso del recinto a las 10:00 hrs).

---

## 📜 3. Plantilla Base a Completar
El agente utiliza el documento oficial [09-Contratos/contrato-arriendo-espacio-manio.md](file:///C:/Users/dinog/OneDrive/Desktop/Proyectos%20de%20Trabajo/Proyecto%20Parcela/09-Contratos/contrato-arriendo-espacio-manio.md) y genera el documento completado para enviar en PDF al cliente con la confirmación de su fecha.
