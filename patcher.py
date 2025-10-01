import os
import json
import base64

jp_excel_list = [
    "CharacterDialogEmojiExcelTable",
    "CharacterDialogFieldExcelTable"
    # "LocalizeCharProfileExcelTable"
    # "LocalizeCCGExcelTable"
    # "LocalizeFieldExcelTable"
]

jp_exceldb_list = [
    "AcademyMessangerExcel",
    "CharacterDialogEmojiExcel",
    "CharacterDialogEventExcel",
    "CharacterDialogExcel",
    "CharacterDialogSubtitleExcel",
    "CharacterVoiceSubtitleExcel",
    "LocalizeCharProfileExcel",
    "LocalizeErrorExcel",
    "LocalizeEtcExcel",
    "LocalizeExcel",
    "LocalizeGachaShopExcel",
    "LocalizeSkillExcel",
    "ScenarioScriptExcel",
    "ScenarioCharacterNameExcel",
    "TutorialCharacterDialogExcel"
]

map = {
    "CharacterDialogEmojiExcelTable": "CharacterDialogEmojiExcel",
    "LocalizeCharProfileExcel": "LocalizeCharProfileExcelTable"
}
excel_dir = os.path.join("JP_excels", "Excel_Dumped")
exceldb_dir = os.path.join("JP_excels", "ExcelDB_Dumped")
output_dir = "output"

if not os.path.exists("JP_excels"):
    os.mkdir("JP_excels")
if not os.path.exists(excel_dir):
    os.mkdir(excel_dir)
if not os.path.exists(exceldb_dir):
    os.mkdir(exceldb_dir)
if not os.path.exists("output"):
    os.mkdir("output")
if not os.path.exists("output/Excel_Dumped"):
    os.mkdir("output/Excel_Dumped")
if not os.path.exists("output/ExcelDB_Dumped"):
    os.mkdir("output/ExcelDB_Dumped")
    


def main():
    locals: dict = json.load(open(os.path.join("data", "gl_locals.json"), encoding='utf-8'))
    for i in jp_excel_list:
        filename = i
        if i in map.keys():
            name = map[i]
        else:
            name = filename
        print(f"Patching excel: {filename}...")
        data = json.load(open(os.path.join(excel_dir, f"{filename}.json"), encoding='utf-8'))
        match filename:
            # for this excel specifically, it appears to not be the same as its exceldb counterpart
            # left here for now...
            case "CharacterDialogEmojiExcelTable":
                for t in data['DataList']:
                    id = f"{name}.{t['GroupId']}.{t['DialogType']}"
                    try:
                        localized = locals[id]
                    except KeyError:
                        continue
                    #t['LocalizeJP'] = localized
            case "CharacterDialogFieldExcelTable":
                for t in data['DataList']:
                    id = f"{name}.{t['GroupId']}.{t['Phase']}"
                    try:
                        localized = locals[id]
                    except KeyError:
                        continue
                    t['LocalizeJP'] = localized
        json.dump(data, open(os.path.join(output_dir, "Excel_Dumped", f"{filename}.json"), 'w', encoding='utf-8'), indent=4, ensure_ascii=False)
    for i in jp_exceldb_list:
        name = i
        filename = i
        if i in map.keys():
            name = map[i]
        else:
            name = filename
        print(f"Patching exceldb: {filename}...")
        data = json.load(open(os.path.join(exceldb_dir, f"{filename}.json"), encoding='utf-8'))
        match filename:
            case "AcademyMessangerExcel":
                for t in data:
                    id = f"{name}.{t['MessageGroupId']}.{t['Id']}"
                    try:
                        localized = locals[id]
                    except KeyError:
                        continue
                    t['MessageJP'] = localized
            case "CharacterDialogEmojiExcel":
                for t in data:
                    id = f"{name}.{t['GroupId']}.{t['DialogType']}"
                    try:
                        localized = locals[id]
                    except KeyError:
                        continue
                    t['LocalizeJP'] = localized
            case "CharacterDialogEventExcel":
                for t in data:
                    id = f"{name}.{t['CostumeUniqueId']}.{t['DisplayOrder']}"
                    try:
                        localized = locals[id]
                    except KeyError:
                        continue
                    t['LocalizeJP'] = localized
            case "CharacterDialogExcel":
                for t in data:
                    id = f"{name}.{t['CharacterId']}.{t['CostumeUniqueId']}.{t['DisplayOrder']}"
                    try:
                        localized = locals[id]
                    except KeyError:
                        continue
                    t['LocalizeJP'] = localized
            case "CharacterDialogSubtitleExcel":
                for t in data:
                    id = f"{name}.{t['CharacterId']}.{t['LocalizeCVGroup']}"
                    try:
                        localized = locals[id]
                    except KeyError:
                        continue
                    t['LocalizeJP'] = localized
            case "CharacterVoiceSubtitleExcel":
                for t in data:
                    id = f"{name}.{t['CharacterVoiceGroupId']}.{t['LocalizeCVGroup']}"
                    try:
                        localized = locals[id]
                    except KeyError:
                        continue
                    t['LocalizeJP'] = localized
            case "LocalizeCharProfileExcel":
                for t in data:
                    id = f"{name}.{t['CharacterId']}"
                    try:
                        full_name = locals[f"{id}.full_name"]
                        status_message = locals[f"{id}.status_message"]
                        family_name = locals[f"{id}.family_name"]
                        personal_name = locals[f"{id}.personal_name"]
                        school_year = locals[f"{id}.school_year"]
                        age = locals[f"{id}.age"]
                        birthday = locals[f"{id}.birthday"]
                        height = locals[f"{id}.height"]
                        designer = locals[f"{id}.designer"]
                        illustrator = locals[f"{id}.illustrator"]
                        hobby = locals[f"{id}.hobby"]
                        weapon_name = locals[f"{id}.weapon_name"]
                        weapon_desc = locals[f"{id}.weapon_desc"]
                        intro = locals[f"{id}.introduction"]
                    except KeyError as e:
                        continue
                    t['StatusMessageJp'] = status_message
                    t['FullNameJp'] = full_name
                    t['FamilyNameJp'] = family_name
                    t['PersonalNameJp'] = personal_name
                    t['SchoolYearJp'] = school_year
                    t['CharacterAgeJp'] = age
                    t['BirthdayJp'] = birthday
                    t['CharHeightJp'] = height
                    t['DesignerNameJp'] = designer
                    t['IllustratorNameJp'] = illustrator
                    t['HobbyJp'] = hobby
                    t['WeaponNameJp'] = weapon_name
                    t['WeaponDescJp'] = weapon_desc
                    t['ProfileIntroductionJp'] = intro
            case "LocalizeErrorExcel":
                for t in data:
                    id = f"{name}.{t['Key']}"
                    try:
                        localized = locals[id]
                    except KeyError:
                        continue
                    t['Jp'] = localized
            case "LocalizeEtcExcel":
                for t in data:
                    id = f"{name}.{t['Key']}"
                    try:
                        s_name = locals[f"{id}.name"]
                        desc = locals[f"{id}.description"]
                    except KeyError:
                        continue
                    t['NameJp'] = s_name
                    t['DescriptionJp'] = desc
            case "LocalizeExcel":
                for t in data:
                    id = f"{name}.{t['Key']}"
                    try:
                        localized = locals[id]
                    except KeyError:
                        continue
                    t['Jp'] = localized
            case "LocalizeGachaShopExcel":
                for t in data:
                    id = f"{name}.{t['GachaShopId']}"
                    try:
                        tab = locals[f"{id}.tab_name"]
                        title = locals[f"{id}.title"]
                        subtitle = locals[f"{id}.subtitle"]
                        desc = locals[f"{id}.description"]
                    except KeyError:
                        continue
                    t['TabNameJp'] = tab
                    t['TitleNameJp'] = title
                    t['SubTitleJp'] = subtitle
                    t['GachaDescriptionJp'] = desc
            case "LocalizeSkillExcel":
                for t in data:
                    id = f"{name}.{t['Key']}"
                    try:
                        s_name = locals[f"{id}.name"]
                        desc = locals[f"{id}.description"]
                    except KeyError:
                        continue
                    t['NameJp'] = s_name
                    t['DescriptionJp'] = desc
            case "ScenarioScriptExcel":
                for t in data:
                    id = f"{name}.{t['GroupId']}.{base64.b64encode(str(t['ScriptKr']).encode()).decode()}"
                    try:
                        localized = locals[id]
                    except KeyError:
                        continue
                    t['TextJp'] = localized
            case "ScenarioCharacterNameExcel":
                for t in data:
                    id = f"{name}.{t['CharacterName']}"
                    try:
                        s_name = locals[f"{id}.name"]
                        nickname = locals[f"{id}.nickname"]
                    except KeyError:
                        continue
                    t['NameJP'] = s_name
                    t['NicknameJP'] = nickname
            case "TutorialCharacterDialogExcel":
                for t in data:
                    id = f"{name}.{t['TalkId']}.{t['VoiceId']}"
                    try:
                        localized = locals[id]
                    except KeyError:
                        continue
                    t['LocalizeJP'] = localized
        json.dump(data, open(os.path.join(output_dir, "ExcelDB_Dumped", f"{filename}.json"), 'w', encoding='utf-8'), indent=4, ensure_ascii=False)
        
if __name__ == '__main__':
    main()