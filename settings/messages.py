

def info_message(version, author):

    message = f"""
    
    <b>Добро пожаловать в приложение CheckMyVin !</b>
    
    Данное приложение разработано для получения информации актуальных отчетов об автомобиле, штрафах, приблизительной оценке ТС
    
    -<b>Версия программы: - </b><i>{version}</i>
    -<b>Разработчик: - </b><i>{author}</i>
    
    """
    return message


def car_report_message(model, vin, date, body_number, color, year, engine_volume, hp,
                       kWt, car_type, passport, owners_list, restrict_dict, dtp_dict,
                       wanted_dict, eaisto_dict):

    message_car = f"""
    
    <b>Отчет об авто {model} {vin} от {date}</b>
    
    -<b>Модель: - </b><i>{model}</i>
    -<b>VIN: - </b><i>{vin}</i>
    -<b>Номер кузова: - </b><i>{body_number}</i>
    -<b>Цвет: - </b><i>{color}</i>
    -<b>Год выпуска: - </b><i>{year}</i>
    -<b>Объем двигателя, см3: - </b><i>{engine_volume}</i>
    -<b>Мощность л.с./кВт: - </b><i>{hp}/{kWt}</i>
    -<b>Тип: - </b><i>{car_type}</i>
    -<b>ПТС: - </b><i>{passport}</i>
    
    """
    
    message_owners_general = f"""
    
    <b>Сведения о собственниках:</b>  
    
    <b>Количество собственников: - </b><i>{len(owners_list)}</i>
    """

    i_owner = 1

    message_owners_detail = """ """

    while i_owner <= len(owners_list):
        cur_owner = owners_list[i_owner - 1]
        cur_owner_info = f"""
        
        <i>{i_owner}й собственник - {cur_owner['simplePersonTypeInfo']}</i>
        
        <b>Предшествующая операция: - </b><i>{cur_owner['lastOperationInfo']}</i>
        
        <b>Период владения: - {cur_owner['period']}</b>
        """

        if cur_owner['to'] == 'null':
            cur_ownership = f"""            
            <i>c {cur_owner['from']} по настоящее время</i>
            """
        else:
            cur_ownership = f"""
            <i>c {cur_owner['from']} по {cur_owner['to']}</i>
            """

        message_owners_detail = message_owners_detail + cur_owner_info + cur_ownership

        i_owner += 1

    message_restricks = """ 
    
    <b>Сведения об ограничениях </b>
    """

    if restrict_dict['count'] == 0:
        message_restricks += """
        
        <i>Ограничения отсутсвуют </i>
        
        """
    else:
        i_restrict = 1
        restrict_list = restrict_dict['records']
        while i_restrict <= len(restrict_list):
            cur_restrict = restrict_list[i_restrict - 1]
            cur_restrict_info = f"""

            <i>Номер ограничения - {cur_restrict['num']}</i>

            <b>Вид ограничения: - {cur_restrict['ogrkodinfo']}</b>
            
            <b>Основание: - {cur_restrict['osnOgr']}</b>

            <b>Дата наложения ограничения: - {cur_restrict['dateogr']}</b>
            
            <b>Дата окончания ограничения: - {cur_restrict['dateadd']}</b>
            """

            message_restricks += cur_restrict_info

            i_restrict += 1

    dtp_message = """ 

        <b>Сведения о ДТП </b>
        """

    if dtp_dict['count'] == 0:
        dtp_message += """

            <i>Сведения о ДТП отсутствуют </i>

            """
    else:
        i_dtp = 1
        dtp_list = dtp_dict['records']
        while i_dtp <= len(dtp_list):
            cur_dtp = dtp_list[i_dtp - 1]
            cur_dtp_info = f"""

                <i>Номер ДТП - {cur_dtp['num']}</i>

                <b>Дата и время ДТП: - {cur_dtp['AccidentDateTime']}</b>
                
                <b>Описание ДТП: - {cur_dtp['DamageDestription']}</b>                

                <b>Место ДТП: - {cur_dtp['AccidentPlace']}</b>
               
                """

            dtp_message += cur_dtp_info

            i_dtp += 1

    wanted_message = """ 

        <b>Сведения о розыске </b>
        """

    if wanted_dict['count'] == 0:
        wanted_message += """

            <i>В розыске не найдено </i>

            """
    else:
        i_wanted = 1
        wanted_list = wanted_dict['records']
        while i_wanted <= len(wanted_list):
            cur_wanted = wanted_list[i_wanted - 1]
            cur_wanted_info = f"""

                <i>Номер розыска - {cur_wanted['num']}</i>

                <b>Регион инициатора розыска: - {cur_wanted['w_reg_inic']}</b>

                <b>Дата постановки в розыск: - {cur_wanted['w_data_pu']}</b>               
              

                """

            wanted_message += cur_wanted_info

            i_wanted += 1

    eaisto_message = """ 

        <b>Сведения о диагностических картах </b>
        """

    if eaisto_dict['count'] == 0:
        eaisto_message += """

            <i>Сведения отсутствуют </i>

            """
    else:
        i_eaisto = 1
        eaisto_list = eaisto_dict['records']
        while i_eaisto <= len(eaisto_list):
            cur_eaisto = eaisto_list[i_eaisto - 1]
            eaisto_message += f"""

                <i>Номер записи - {cur_eaisto['num']}</i>

                <b>Дата окончания диагностической карты: - </b><i>{cur_eaisto['dcExpirationDate']}</i>

                <b>Пункт выдачи диагностической карты: - </b><i>{cur_eaisto['pointAddress']}</i> 
                              
                <b>Номер диагностической карты: - </b><i>{cur_eaisto['dcNumber']}</i>   
                            
                <b>Показания одометра: - </b><i>{cur_eaisto['odometerValue']}</i>               


                """

            for item in cur_eaisto['previousDcs']:
                eaisto_message += f"""
                    
                <b>Предыдущее значение одометра: - </b><i>{item['dcNumber']}</i>    
                <b>Номер диагностической карты: - </b><i>{item['dcNumber']}</i> 
                
                """

            i_eaisto += 1


    message = message_car + message_owners_general + message_owners_detail \
              + message_restricks + dtp_message + wanted_message + eaisto_message

    print('отчет по авто готов')
    return message
