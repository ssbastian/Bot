#
import yaml
import os
from pathlib import Path

def merge_domain_files():
    """Une los archivos domain según TU estructura preferida"""
    
    domain_files = [
        'domain/domain_despedida.yml',
        'domain/domain_activ_emoc.yml',
        'domain/domain_alternativas.yml', 
        # 'domain/responses.yml',         
        # 'domain/entities_actions.yml',  
        # 'domain/session_config.yml'     
    ]
    
    merged_domain = {'version': '3.1'}
    
    print("🔍 Uniendo archivos domain...")
    
    for file_path in domain_files:
        if os.path.exists(file_path):
            print(f"📂 Leyendo: {file_path}")
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = yaml.safe_load(f) or {}
                    
                    for key, value in content.items():
                        if key in merged_domain:
                            # Combinar listas
                            if isinstance(value, list):
                                merged_domain[key].extend(value)
                            # Combinar diccionarios
                            elif isinstance(value, dict):
                                merged_domain[key].update(value)
                            else:
                                merged_domain[key] = value
                        else:
                            merged_domain[key] = value
                            
            except Exception as e:
                print(f"❌ Error en {file_path}: {e}")
        else:
            print(f"⏭️  Saltando: {file_path} (no existe)")
    
    # Eliminar duplicados
    for key in ['intents', 'actions', 'entities']:
        if key in merged_domain and isinstance(merged_domain[key], list):
            merged_domain[key] = list(dict.fromkeys(merged_domain[key]))
    
    # Guardar domain unificado
    with open('domain.yml', 'w', encoding='utf-8') as f:
        yaml.dump(merged_domain, f, allow_unicode=True, sort_keys=False, width=1000)
    
    print("✅ domain.yml creado exitosamente!")
    return True

if __name__ == "__main__":
    merge_domain_files()