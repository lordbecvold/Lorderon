function get_random_vnum_from_table(items)
	local temp_table = {}
	local playerLevel = pc.get_level()
	table.foreachi(items, 
		function(index, item)
			local itemProbability = item[2]
			local itemVnum = item[1]
			local meetsLevelLimit = true
			if table.getn(item) > 2 then 
				if playerLevel < item[3] then
					meetsLevelLimit = false
				end
				if table.getn(item) > 3 then 
					if playerLevel > item[4] then
						meetsLevelLimit = false
					end
				end
			end
			if meetsLevelLimit then
				for amount = 1, itemProbability do
					table.insert(temp_table, itemVnum)
				end
			end
		end
	)
	return temp_table[math.random(table.getn(temp_table))]
end

function get_time_remaining(seconds)
	if seconds <= 60 then
		return string.format(gameforge.locale.time.seconds, seconds)
	else
		local minutes = math.floor(seconds / 60)
		seconds = math.mod(seconds, 60)
		if minutes <= 60 then
			return string.format(gameforge.locale.time.minutes_and_seconds, minutes, seconds)
		else
			local hours = math.floor(minutes / 60)
			minutes = math.mod(minutes, 60)
			if hours <= 24 then
				return string.format(gameforge.locale.time.hours_and_minutes, hours, minutes)
			else
				local days = math.floor(hours / 24)
				hours = math.mod(hours, 24)
				return string.format(gameforge.locale.time.days_and_hours, days, hours)
			end
		end
	end
end

function count_item_range(firstVnum, lastVnum)
    local amount = 0
    for item = firstVnum, lastVnum, 1 do
         local i = pc.count_item(item)
         amount = amount + i
    end
    return amount
end

function remove_item_range(amountLeft, firstVnum, lastVnum)
	if count_item_range(firstVnum, lastVnum) < amountLeft then
		return false
	end
	for currentVnum = firstVnum, lastVnum, 1 do
		local currentAmount = pc.count_item(currentVnum)
		if currentAmount > 0 then
			if currentAmount < amountLeft then
				pc.remove_item(currentVnum, currentAmount)
				amountLeft = amountLeft - currentAmount
			else
				pc.remove_item(currentVnum, amountLeft)
				return true
			end
		end
	end
end

function is_destination_village(maps)
	local map_lookup = {}
	if maps == 1 then
	    map_lookup = {[1]='', [21]='', [41]='' }
	elseif maps==2 then
	    map_lookup = {[3]='', [23]='', [43]='' }
	elseif maps==3 then
        map_lookup = {[1]='', [21]='', [41]='',[3]='', [23]='', [43]='' }
	elseif maps==65 then
        map_lookup = {[65]='' }
	end
	return map_lookup[pc.get_map_index()]
end
function say_important_title(name) say(color256(255, 230, 186)..name..color256(196, 196, 196)) end
function say_important(name) say(color256(255, 230, 186)..name..color256(196, 196, 196)) end
