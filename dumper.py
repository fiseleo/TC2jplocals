import os
import json
import base64

gl_excel_list = [
    "CharacterDialogFieldExcelTable",
    "LocalizeCharProfileExcelTable"
]
gl_exceldb_list = [
    "AcademyMessangerExcel",
    "CharacterDialogEmojiExcel",
    "CharacterDialogEventExcel",
    "CharacterDialogExcel",
    "CharacterDialogSubtitleExcel",
    "CharacterVoiceSubtitleExcel",
    "LocalizeErrorExcel",
    "LocalizeEtcExcel",
    "LocalizeExcel",
    "LocalizeGachaShopExcel",
    "LocalizeSkillExcel",
    "ScenarioScriptExcel",
    "ScenarioCharacterNameExcel",
    "TutorialCharacterDialogExcel"
]


if not os.path.exists("TW_excels"):
    os.mkdir("TW_excels")

excel_dir = os.path.join("TW_excels", "Excel_Dumped")
if not os.path.exists(excel_dir):
    os.mkdir(excel_dir)


exceldb_dir = os.path.join("TW_excels", "ExcelDB_Dumped")
if not os.path.exists(exceldb_dir):
    os.mkdir(exceldb_dir)



if not os.path.exists("data"):
    os.mkdir("data")

data_path = os.path.join("data", "gl_locals.json")

translation = {}

def main():
    for i in gl_excel_list:
        full_path = os.path.join(excel_dir, f"{i}.json")
        data = json.load(open(full_path, encoding='utf-8'))
        match i:
            case "CharacterDialogFieldExcelTable":
                for t in data['DataList']:
                    translation[f"{i}.{t['GroupId']}.{t['Phase']}"] = t['LocalizeTW']
            case "LocalizeCharProfileExcelTable":
                for t in data['DataList']:
                    translation[f"{i}.{t['CharacterId']}.full_name"] = t['FullNameTw']
                    translation[f"{i}.{t['CharacterId']}.status_message"] = t['StatusMessageTw']
                    translation[f"{i}.{t['CharacterId']}.family_name"] = t['FamilyNameTw']
                    translation[f"{i}.{t['CharacterId']}.personal_name"] = t['PersonalNameTw']
                    translation[f"{i}.{t['CharacterId']}.school_year"] = t['SchoolYearTw']
                    translation[f"{i}.{t['CharacterId']}.age"] = t['CharacterAgeTw']
                    translation[f"{i}.{t['CharacterId']}.birthday"] = t['BirthdayTw']
                    translation[f"{i}.{t['CharacterId']}.height"] = t['CharHeightTw']
                    translation[f"{i}.{t['CharacterId']}.designer"] = t['DesignerNameTw']
                    translation[f"{i}.{t['CharacterId']}.illustrator"] = t['IllustratorNameTw']
                    translation[f"{i}.{t['CharacterId']}.hobby"] = t['HobbyTw']
                    translation[f"{i}.{t['CharacterId']}.weapon_name"] = t['WeaponNameTw']
                    translation[f"{i}.{t['CharacterId']}.weapon_desc"] = t['WeaponDescTw']
                    translation[f"{i}.{t['CharacterId']}.introduction"] = t['ProfileIntroductionTw']
    for i in gl_exceldb_list:
        full_path = os.path.join(exceldb_dir, f"{i}.json")
        data = json.load(open(full_path, encoding='utf-8'))
        match i:
            case "AcademyMessangerExcel":
                for t in data:
                    translation[f"{i}.{t['MessageGroupId']}.{t['Id']}"] = t['MessageTW']
            case "CharacterDialogEmojiExcel":
                for t in data:
                    translation[f"{i}.{t['GroupId']}.{t['DialogType']}"] = t['LocalizeTW']
            case "CharacterDialogEventExcel":
                for t in data:
                    translation[f"{i}.{t['CostumeUniqueId']}.{t['DisplayOrder']}"] = t['LocalizeTW']
            case "CharacterDialogExcel":
                for t in data:
                    translation[f"{i}.{t['CharacterId']}.{t['CostumeUniqueId']}.{t['DisplayOrder']}"] = t['LocalizeTW']
            case "CharacterDialogSubtitleExcel":
                for t in data:
                    translation[f"{i}.{t['CharacterId']}.{t['LocalizeCVGroup']}"] = t['LocalizeTW']
            case "CharacterVoiceSubtitleExcel":
                for t in data:
                    translation[f"{i}.{t['CharacterVoiceGroupId']}.{t['LocalizeCVGroup']}"] = t['LocalizeTW']
            case "LocalizeErrorExcel":
                for t in data:
                    translation[f"{i}.{t['Key']}"] = t['Tw']
            case "LocalizeEtcExcel":
                for t in data:
                    translation[f"{i}.{t['Key']}.name"] = t['NameTw']
                    translation[f"{i}.{t['Key']}.description"] = t['DescriptionTw']
            case "LocalizeExcel":
                for t in data:
                    translation[f"{i}.{t['Key']}"] = t['Tw']
            case "LocalizeGachaShopExcel":
                for t in data:
                    translation[f"{i}.{t['GachaShopId']}.tab_name"] = t['TabNameTw']
                    translation[f"{i}.{t['GachaShopId']}.title"] = t['TitleNameTw']
                    translation[f"{i}.{t['GachaShopId']}.subtitle"] = t['SubTitleTw']
                    translation[f"{i}.{t['GachaShopId']}.description"] = t['GachaDescriptionTw']
            case "LocalizeSkillExcel":
                for t in data:
                    translation[f"{i}.{t['Key']}.name"] = t['NameTw']
                    translation[f"{i}.{t['Key']}.description"] = t['DescriptionTw']
                    #Todo NameTw 為空 和 'DescriptionTw 為空 要刪除
                    if t['NameTw'] == "" and t['DescriptionTw'] == "":
                        del translation[f"{i}.{t['Key']}.name"]
                        del translation[f"{i}.{t['Key']}.description"]

            case "ScenarioScriptExcel":
                for t in data:
                    translation[f"{i}.{t['GroupId']}.{base64.b64encode(str(t['ScriptKr']).encode()).decode()}"] = t['TextTw']
            case "ScenarioCharacterNameExcel":
                for t in data:
                    translation[f"{i}.{t['CharacterName']}.name"] = t['NameTW']
                    translation[f"{i}.{t['CharacterName']}.nickname"] = t['NicknameTW']
            case "TutorialCharacterDialogExcel":
                for t in data:
                    translation[f"{i}.{t['TalkId']}.{t['VoiceId']}"] = t['LocalizeTW']
    json.dump(translation, open(data_path, 'w', encoding='utf-8'), indent=4, ensure_ascii=False)
    
if __name__ == '__main__':
    main()