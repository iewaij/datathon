import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import set_matplotlib_formats

# cosmetic options for matplotlib and seaborn
set_matplotlib_formats("svg")
rc = {
    "figure.figsize": (6.4, 4.8),
    "figure.dpi": 300,
    "axes.titlesize": "large",
    "axes.titleweight": "bold",
    "axes.titlepad": 12,
    "axes.titlelocation": "left",
}

sns.set_theme(context="notebook", style="darkgrid", color_codes=True, rc=rc)
pd.set_option("max_columns", None)
pd.set_option("max_colwidth", None)

loans = pd.read_csv(
    "data/loans.csv",
    names=[
        "loan_id",
        "loan_name",
        "original_language",
        "description",
        "description_translated",
        "funded_amount",
        "loan_amount",
        "status",
        "image_id",
        "video_id",
        "activity_name",
        "sector_name",
        "loan_use",
        "country_code",
        "country_name",
        "town_name",
        "currency_policy",
        "currency_exchange_coverage_rate",
        "currency",
        "partner_id",
        "posted_time",
        "planned_expiration_time",
        "disburse_time",
        "raised_time",
        "lender_term",
        "num_lenders_total",
        "num_journal_entries",
        "num_bulk_entries",
        "tags",
        "borrower_names",
        "borrower_genders",
        "borrower_pictured",
        "repayment_interval",
        "distribution_model",
    ],
    header=0,
)
lenders = pd.read_csv(
    "data/lenders.csv",
    names=[
        "permanent_name",
        "display_name",
        "main_pic_id",
        "city",
        "state",
        "country_code",
        "member_since",
        "personal_url",
        "occupation",
        "loan_because",
        "other_info",
        "loan_purchase_num",
        "invited_by",
        "num_invited",
    ],
    header=0,
)
loans_lenders = pd.read_csv("data/loans_lenders.csv", names=["loan_id", "lenders"])
country_econ = pd.read_csv(
    "data/country_econ.csv",
    sep=";",
    names=[
        "area",
        "country_name",
        "lat",
        "longitude",
        "long_name",
        "mer1990_40",
        "mer1995_40",
        "mer2000_40",
        "mer2005_40",
        "new_countryid",
        "popgpw_1990_40",
        "popgpw_1995_40",
        "popgpw_2000_40",
        "popgpw_2005_40",
        "ppp1990_40",
        "ppp1995_40",
        "ppp2000_40",
        "ppp2005_40",
        "quality",
        "rig",
        "quality_revision",
        "date_of_last",
    ],
    header=0,
)
country_stats = pd.read_csv(
    "data/country_stats.csv",
    names=[
        "alternative_country_name",
        "country_code",
        "country_code_3",
        "continent",
        "region",
        "population",
        "population_below_poverty_line",
        "hdi",
        "life_expectancy",
        "expected_years_of_schooling",
        "mean_years_of_schooling",
        "gni",
        "country_name",
    ],
    header=0,
)

loans_amount = loans[["country_name", "loan_amount"]]
country_ppl = country_stats[["country_name", "population"]]
loans_ppl = (
    loans_amount.merge(country_ppl, on=["country_name"]).groupby("country_name").sum()
)
loans_ppl_plot = sns.regplot(data=loans_ppl, x="loan_amount", y="population")
