from project3.influencers.premium_influencer import PremiumInfluencer
from project3.influencers.standard_influencer import StandardInfluencer
from project3.campaigns.high_budget_campaign import HighBudgetCampaign
from project3.campaigns.low_budget_campaign import LowBudgetCampaign


class InfluencerManagerApp:
    valid_influencers_types = {"PremiumInfluencer": PremiumInfluencer,
                               "StandardInfluencer": StandardInfluencer}

    valid_campaign_types = {"HighBudgetCampaign": HighBudgetCampaign,
                            "LowBudgetCampaign": LowBudgetCampaign}

    def __init__(self):
        self.influencers = []
        self.campaigns = []

    def register_influencer(self,
                            influencer_type: str,
                            username: str,
                            followers: int,
                            engagement_rate: float) -> str:

        if influencer_type not in self.valid_influencers_types:
            return f"{influencer_type} is not an allowed influencer type."

        for influencer in self.influencers:
            if influencer.username == username:
                return f"{username} is already registered."

        influencer = self.valid_influencers_types[influencer_type](username, followers, engagement_rate)
        self.influencers.append(influencer)

        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self,
                        campaign_type: str,
                        campaign_id: int,
                        brand: str,
                        required_engagement: float) -> str:

        if campaign_type not in self.valid_campaign_types:
            return f"{campaign_type} is not a valid campaign type."

        for campaign in self.campaigns:
            if campaign.campaign_id == campaign_id:
                return f"Campaign ID {campaign_id} has already been created."

        campaign = self.valid_campaign_types[campaign_type](campaign_id, brand, required_engagement)
        self.campaigns.append(campaign)

        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer = self._get_influencer(influencer_username)
        campaign = self._get_campaign(campaign_id)

        if not influencer:
            return f"Influencer '{influencer_username}' not found."

        if not campaign:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return (f"Influencer '{influencer_username}' does not meet the eligibility criteria "
                    f"for the campaign with ID {campaign_id}.")

        influencer_payment = influencer.calculate_payment(campaign)
        if influencer_payment > 0.0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= influencer_payment
            influencer.campaigns_participated.append(campaign)
            return (f"Influencer '{influencer_username}' has successfully participated "
                    f"in the campaign with ID {campaign_id}.")

    def calculate_total_reached_followers(self):
        total_reached_followers = {}
        for influencers in self.influencers:
            for campaign in influencers.campaigns_participated:
                reached_followers = influencers.reached_followers(type(campaign).__name__)
                total_reached_followers[campaign] = total_reached_followers.get(campaign, 0) + reached_followers

        return total_reached_followers

    def influencer_campaign_report(self, username: str):
        influencers = self._get_influencer(username)
        if influencers:
            return influencers.display_campaigns_participated()

    def campaign_statistics(self):
        total_reached_followers = self.calculate_total_reached_followers()

        sorted_campaigns = sorted(self.campaigns, key=lambda x: (len(x.approved_influencers), -x.budget))

        campaign_stats = [
            f"  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)}, "
            f"Total budget: ${campaign.budget:.2f}, Total reached followers: {total_reached_followers.get(campaign, 0)}"
            for campaign in sorted_campaigns
        ]

        return f"$$ Campaign Statistics $$\n" + "\n".join(campaign_stats)

    def _get_influencer(self, username: str):
        influencer = [i for i in self.influencers if i.username == username]
        return influencer[0] if influencer else None

    def _get_campaign(self, campaign_id: int):
        campaign = [c for c in self.campaigns if c.campaign_id == campaign_id]
        return campaign[0] if campaign else None




