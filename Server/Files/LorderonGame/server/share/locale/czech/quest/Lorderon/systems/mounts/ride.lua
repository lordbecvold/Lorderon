quest ride begin
	state start begin
		function GetRideInfo(vnum)
			if ride.ride_info==nil then
				ride.ride_info = {
					--------------------------------------------------------------------------------------------------------------------------------------------------------------
					[71164]= { ["mount_vnum"] = 20109,	["duration"] = 60*60*24*365,		["bonus_id"] = apply.MOV_SPEED,	["bonus_value"] = 20,	["req_level"] = 1,	},
					[71125]= { ["mount_vnum"] = 20205,	["duration"] = 60*60*24*365,		["bonus_id"] = apply.ATTBONUS_MONSTER,	["bonus_value"] = 10,	["req_level"] = 1,	},
					[71128]= { ["mount_vnum"] = 20208,	["duration"] = 60*60*24*365,		["bonus_id"] = apply.ATTBONUS_MONSTER,	["bonus_value"] = 15,	["req_level"] = 1,	},
					[71222]= { ["mount_vnum"] = 20114,	["duration"] = 60*60*24*365,		["bonus_id"] = apply.ATTBONUS_MONSTER,	["bonus_value"] = 20,	["req_level"] = 1,	},
					[71224]= { ["mount_vnum"] = 20227,	["duration"] = 60*60*24*365,		["bonus_id"] = apply.ATTBONUS_MONSTER,	["bonus_value"] = 25,	["req_level"] = 1,	},
					[71225]= { ["mount_vnum"] = 20119,	["duration"] = 60*60*24*365,		["bonus_id"] = apply.ATTBONUS_MONSTER,	["bonus_value"] = 30,	["req_level"] = 1,	},
					--------------------------------------------------------------------------------------------------------------------------------------------------------------
				}
			end
			return ride.ride_info[vnum]
		end

		function Ride(vnum, remain_time)
			local mount_info = ride.GetRideInfo(vnum)
			if mount_info==nil then return end

			if pc.level < mount_info["req_level"] then
				syschat("Nemáš dostateènou úrovìò na použítí pøedmìtu")
			else
				if 112 == pc.get_map_index() then 
					return
				end

				if remain_time==0 then
					if mount_info["duration"] <= 0 then
						if item.is_available0() then
							remain_time = item.get_socket(0)
						else
							remain_time = 60
						end
					else
						remain_time = mount_info["duration"]
					end
				end

				pc.mount(mount_info["mount_vnum"], remain_time)
				pc.mount_bonus(mount_info["bonus_id"], mount_info["bonus_value"], remain_time)
			end
		end

		when login begin
			local vnum, remain_time = pc.get_special_ride_vnum()
			if vnum==0 then return end

			local mount_info = ride.GetRideInfo(vnum)
			if mount_info==nil then return end

			ride.Ride(vnum, remain_time)
		end

		when
		-------------------------------------------------------------------------------------------------------------------
		71164.use or 71125.use or 71128.use or 71222.use or 71224.use or 71225.use
		-------------------------------------------------------------------------------------------------------------------
		begin
			if pc.is_polymorphed() then
				syschat("Nemùžeš použít pøedmìt když jsi v promìnì!")
			elseif not pc.is_riding() then
				if horse.is_summon() then
					horse.unsummon()
				end
				ride.Ride(item.vnum, 0)
			end
		end
	end
end
