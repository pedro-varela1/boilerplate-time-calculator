def add_time(start, duration, *d):
        start = start.split()
        start[0] = start[0].split(':')
        duration = duration.split()
        duration[0] = duration[0].split(':')

        if start[1] == 'PM':
                start[0][0] = str(int(start[0][0])+12)

        day_number = int((int(duration[0][0]) + int(start[0][0]) + int((int(duration[0][1]) + int(start[0][1]))/60))/24)
        if day_number == 1:
                day = '(next day)'
        elif day_number == 0:
                day = ''
        else:
                day = '(' + str(day_number) + ' days later)'
        hour = int((int(duration[0][0]) + int(start[0][0]) + int((int(duration[0][1]) + int(start[0][1]))/60)) % 24)
        if hour >= 13:
                hour = str(hour - 12)
                complement = 'PM'
        elif hour == 12:
                hour = str(hour)
                complement = 'PM'
        else:
                if hour==0:
                        hour = 12
                hour = str(hour)
                complement = 'AM'
        min = str(int((int(duration[0][1]) + int(start[0][1])) % 60)).zfill(2)

        result = hour + ':' + min + ' ' + complement + ' ' + day

        #
        week = dict()
        week[1] = 'monday'
        week[2] = 'tuesday'
        week[3] = 'wednesday'
        week[4] = 'thursday'
        week[5] = 'friday'
        week[6] = 'saturday'
        week[7] = 'sunday'

        day_index = 0
        for dia in d:
                if type(dia) == str:
                        for i,day_word in week.items():
                                if day_word == dia.lower():
                                        day_index = i
                                        break
                        day_index = int((day_index+day_number) % 7)
                        if day_index == 0:
                                day_index = 7
                        result = hour + ':' + min + ' ' + complement + ', ' + week[day_index].capitalize() + ' ' + day
        return result.rstrip()
