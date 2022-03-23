#Lorderon Client Dev By Lordbecvold
import uiScriptLocale

window = {
	"name" : "GuildWindow_BoardPage",
	"x" : 8,
	"y" : 30,
	"width" : 360,
	"height" : 298,
	"children" :
	(
		{
			"name" : "GradeNumber", "type" : "text", "x" : 21, "y" : 5, "text" : uiScriptLocale.GUILD_GRADE_NUM,
		},
		{
			"name" : "GradeName", "type" : "text", "x" : 76, "y" : 5, "text" : uiScriptLocale.GUILD_GRADE_RANK,
		},
		{
			"name" : "InviteAuthority", "type" : "text", "x" : 126, "y" : 5, "text" : uiScriptLocale.GUILD_GRADE_PERMISSION_JOIN,
		},
		{
			"name" : "DriveOutAuthority", "type" : "text", "x" : 183, "y" : 5, "text" : uiScriptLocale.GUILD_GRADE_PERMISSION_DELETE,
		},
		{
			"name" : "NoticeAuthority", "type" : "text", "x" : 240, "y" : 5, "text" : uiScriptLocale.GUILD_GRADE_PERMISSION_NOTICE,
		},
		{
			"name" : "SkillAuthority", "type" : "text", "x" : 297, "y" : 5, "text" : uiScriptLocale.GUILD_GRADE_PERMISSION_SKILL,
		},
	),
}
