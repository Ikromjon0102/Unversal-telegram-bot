from aiogram import Dispatcher

from loader import dp
from .adminfilter import IsAdmin
from .groupfilter import IsGroup
from .shaxsiyfilter import IsPrivate


if __name__ == "filters":
    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)
