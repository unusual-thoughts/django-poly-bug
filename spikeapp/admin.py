from django.contrib import admin

from polymorphic.admin import PolymorphicInlineSupportMixin, StackedPolymorphicInline
from .models import Order, Payment, CreditCardPayment, BankPayment, SepaPayment, Beneficiary, TestPayment


class CreditCardPaymentInline(StackedPolymorphicInline.Child):
    model = CreditCardPayment


class BankPaymentInline(StackedPolymorphicInline.Child):
    model = BankPayment


class SepaPaymentInline(StackedPolymorphicInline.Child):
    model = SepaPayment
    filter_horizontal = ('beneficiaries',)

class TestPaymentInline(StackedPolymorphicInline.Child):
    model = TestPayment

class PaymentInline(StackedPolymorphicInline):
    """
    An inline for a polymorphic model.
    The actual form appearance of each row is determined by
    the child inline that corresponds with the actual model type.
    """

    model = Payment
    child_inlines = (
        CreditCardPaymentInline,
        BankPaymentInline,
        SepaPaymentInline,
        TestPaymentInline
    )


@admin.register(Order)
class OrderAdmin(PolymorphicInlineSupportMixin, admin.ModelAdmin):
    """
    Admin for orders.
    The inline is polymorphic.
    To make sure the inlines are properly handled,
    the ``PolymorphicInlineSupportMixin`` is needed to
    """
    inlines = (PaymentInline,)


@admin.register(Beneficiary)
class BeneficiaryAdmin(admin.ModelAdmin):
    model = Beneficiary