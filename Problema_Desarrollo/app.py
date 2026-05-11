from infrastructure.audit_logger import obtener_auditor
from entities.patient import Paciente
from entities.treatment import Telemedicina, ProcedimientoQuirurgico
from entities.appointment import CitaMedica
from core_exceptions.medical_errors import VitalisHubError

auditor = obtener_auditor()

def ejecutar_flujo(id_op, funcion):
    print(f"\n[EVALUANDO CASO MÉDICO #{id_op}]")
    try:
        resultado = funcion()
        auditor.info(f"Caso #{id_op} procesado correctamente.")
    except VitalisHubError as ve:
        auditor.warning(f"Incidencia Médica en Caso #{id_op}: {ve}")
        print(f"NOTIFICACIÓN SISTEMA: {ve}")
    except Exception as e:
        auditor.error(f"FALLO CRÍTICO en Caso #{id_op}: {e}", exc_info=True)
        print("ESTADO: Sistema Vitalis en modo contingencia (activo).")
    finally:
        print(f"--- Fin de revisión Caso #{id_op} ---")

def iniciar_simulacion():
    casos = []
    
    # 1. Paciente válido
    casos.append(lambda: print(f"Registrado: {Paciente('VITAL-99', 'Ana Polo', 'ana@med.com').nombre_completo}"))
    
    # 2. ID inválido (contiene caracteres especiales)
    casos.append(lambda: Paciente("VITAL-99!!", "Error", "e@e.com"))
    
    # 3. Telemedicina exitosa
    consulta = Telemedicina("Dermatología Digital", 80.0)
    paciente_a = Paciente("P001", "Luis Jara", "luis@mail.com")
    cita1 = CitaMedica(paciente_a, consulta, {'minutos': 30, 'conexion_estable': True})
    casos.append(lambda: cita1.autorizar_cita())

    # 4. Telemedicina fallida (Sin conexión)
    cita2 = CitaMedica(paciente_a, consulta, {'conexion_estable': False})
    casos.append(lambda: cita2.autorizar_cita())

    # 5. Cirugía exitosa (complejidad y insumos)
    cirugia = ProcedimientoQuirurgico("Apendicectomía", 5000.0)
    cita3 = CitaMedica(paciente_a, cirugia, {'complejidad': 2, 'insumos': 1500, 'ayuno_completo': True})
    casos.append(lambda: cita3.autorizar_cita())

    # 6. Cirugía fallida (Sin ayuno)
    cita4 = CitaMedica(paciente_a, cirugia, {'ayuno_completo': False})
    casos.append(lambda: cita4.autorizar_cita())

    # 7. Error de parámetros (TypeError controlado)
    casos.append(lambda: consulta.tasar_servicio(minutos="treinta"))

    # 8. Email inválido
    casos.append(lambda: Paciente("P002", "Marta", "marta.com"))

    # 9. Consulta nocturna (Sobrecarga de método)
    casos.append(lambda: print(f"Costo Nocturno: {consulta.tasar_servicio(nocturno=True)}"))

    # 10. Registro exitoso de folio
    casos.append(lambda: print(f"Folio Generado: {consulta.folio}"))

    for i, caso in enumerate(casos, 1):
        ejecutar_flujo(i, caso)

if __name__ == "__main__":
    print("VITALIS HEALTH HUB - SISTEMA DE AUDITORÍA CLÍNICA")
    iniciar_simulacion()