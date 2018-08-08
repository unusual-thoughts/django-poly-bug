from django.db import models
from django.utils.dates import MONTHS_3
from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from polymorphic.models import PolymorphicModel


@python_2_unicode_compatible
class Order(models.Model):
    """
    An example order that has polymorphic relations
    """
    title = models.CharField(_("Title"), max_length=200)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        ordering = ('title',)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Payment(PolymorphicModel):
    """
    A generic payment model.
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(default=0, blank=True, max_digits=10, decimal_places=2)
    index = models.PositiveIntegerField(default=0, blank=False)

    class Meta:
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")
        ordering = ('index',)

    def __str__(self):
        return "${0}".format(self.amount)


class CreditCardPayment(Payment):
    """
    Credit card
    """
    card_type = models.CharField(max_length=10)

    class Meta:
        verbose_name = _("Credit Card Payment")
        verbose_name_plural = _("Credit Card Payments")


class BankPayment(Payment):
    """
    Payment by bank
    """
    bank_name = models.CharField(max_length=100)
    swift = models.CharField(max_length=20)

    class Meta:
        verbose_name = _("Bank Payment")
        verbose_name_plural = _("Bank Payments")


class Beneficiary(models.Model):
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)

    class Meta:
        verbose_name = _("SEPA beneficiary")
        verbose_name_plural = _("SEPA Beneficiaries")

    def __str__(self):
        return "{0} {1}".format(self.firstname, self.lastname)


class SepaPayment(Payment):
    """
    Payment by SEPA (EU)
    """
    iban = models.CharField(max_length=34)
    bic = models.CharField(max_length=11)
    beneficiaries = models.ManyToManyField(Beneficiary, "sepa", blank=True)

    class Meta:
        verbose_name = _("SEPA Payment")
        verbose_name_plural = _("SEPA Payments")

class TestPayment(Payment):
    title = models.CharField(max_length=34)
    beneficiaries = models.ForeignKey(Beneficiary, "test", blank=True)

    class Meta:
        verbose_name = _("Test Payment")
        verbose_name_plural = _("Test Payments")
