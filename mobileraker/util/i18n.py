
from typing import Dict
from mobileraker.data.dtos.mobileraker.notification_config_dto import DeviceNotificationEntry
from mobileraker.data.dtos.moonraker.printer_snapshot import PrinterSnapshot
from mobileraker.util.configs import CompanionLocalConfig

from mobileraker.util.notification_placeholders import replace_placeholders

# List of available tokens
# printer_name - The name of the printer
# progress - Only available if printing, the progress of the current print in %
# eta - Only if printing, the ETA in hh:mm## STIL WIP!
# file - Only if printing, the file that is currently printing

_mobileraker_en: Dict[str, str] = {
    'print_progress_title': 'Print progress of $printer_name',
    'print_progress_body': '$progress, ETA: $a_eta, Layer: $cur_layer/$max_layer',
    'state_title': 'State of $printer_name changed',
    'state_printing_body': 'Started to print file: "$file"',
    'state_paused_body': 'Paused while printing file: "$file"',
    'state_completed_body': 'Finished printing: "$file"',
    'state_error_body': 'Error while printing file: "$file"',
    'state_standby_body': 'Printer is in Standby',
    'm117_custom_title': 'User Notification'
}

_mobileraker_de: Dict[str, str] = {
    'print_progress_title': 'Druck-Fortschritt von $printer_name',
    'print_progress_body': '$progress, ETA: $a_eta',
    'state_title': 'Status von $printer_name geändert',
    'state_printing_body': 'Starte Druck der Datei: "$file"',
    'state_paused_body': 'Druck der Datei pausiert: "$file"',
    'state_completed_body': 'Druck abgeschlossen: "$file"',
    'state_error_body': 'Fehler beim Drucken der Datei: "$file"',
    'state_standby_body': 'Drucker im Standby',
    'm117_custom_title': 'Nutzer-Benachrichtigung'
}


_mobileraker_hu: Dict[str, str] = {

}
    
_mobileraker_uk: Dict[str, str] = {
    'print_progress_title': 'Прогрес друку $printer_name',
    'print_progress_body': '$progress, ETA: $a_eta, Шар: $cur_layer/$max_layer',
    'state_title': 'Стан $printer_name змінився',
    'state_printing_body': 'Почав друкувати файл: "$file"',
    'state_paused_body': 'Призупинено під час друку файлу: "$file"',
    'state_completed_body': 'Друк завершено: "$file"',
    'state_error_body': 'Помилка під час друку файлу: "$file"',
    'state_standby_body': 'Принтер у режимі очікування',
    'm117_custom_title': 'Сповіщення користувача'
}

_mobileraker_chtw: Dict[str, str] = {

}

_mobileraker_cnch: Dict[str, str] = {

}


languages: Dict[str, Dict[str, str]] = {
    'de': _mobileraker_de,
    'en': _mobileraker_en,
    'hu': _mobileraker_hu,
    'uk': _mobileraker_uk,
    'cn': _mobileraker_cnch,
    'cntw': _mobileraker_chtw,

}


def translate(country_code: str, str_key: str) -> str:
    if country_code not in languages:
        # fallback to en
        return translate('en', str_key)
    translations = languages[country_code]
    if str_key not in translations:
        if country_code == 'en':
            raise AttributeError('No language-entry found for "%s"', str_key)
        # fallback to en
        return translate('en', str_key)
    translation = translations[str_key]

    return translation


def translate_replace_placeholders(str_key: str, cfg: DeviceNotificationEntry, snap: PrinterSnapshot, companion_config: CompanionLocalConfig) -> str:
    # For now users can only globally define the notification language!
    translation = translate(companion_config.language, str_key)
    # translation = translate(cfg.language, str_key)
    return replace_placeholders(translation, cfg, snap, companion_config)
