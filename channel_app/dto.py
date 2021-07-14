from channel_app.models import Channel, Price, Discount


class ChannelDto:
    pass


def get_channel_dto(channels):
    lst = []
    for channel in channels:
        channel_dto = ChannelDto()
        channel_dto.id = channel.id
        channel_dto.name = channel.name
        channel_dto.photo = channel.photo
        channel_dto.price = Price.objects.get(channel=channel).price
        channel_dto.discount = Discount.objects.filter(channel=channel)
        lst.append(channel_dto)
    return lst
