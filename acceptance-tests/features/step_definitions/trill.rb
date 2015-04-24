Given(/^I am a User$/) do
  pending # Write code here that turns the phrase above into concrete actions
  #Get a connection to a database. 
  #Add Forename & Surname to db.
  #Add any other data required by the db.
  #Do we need to clean up afterwards.
end

Given(/^I have a Role$/) do
  pending # Write code here that turns the phrase above into concrete actions
  #Get a connection to a database.
  #Ensure Forename & Surname exists on db.
  #Add role is added to db.
  #Ensure role is linked to forename/surname
  #Add any other data required by the db.
  #Do we need to clean up afterwards.
end

Given(/^I do not have a Role$/) do
  pending # Write code here that turns the phrase above into concrete actions
  #Can user have no role ie: set to nil/null?
  #Can role be gibberish?
end

Given(/^I have Skills$/) do
  pending # Write code here that turns the phrase above into concrete actions
  #Get a connection to a database.
  #Ensure role exists on db.
  #Add skill to db.
  #Ensure skill is linked to role.
  #Add any other data required by the db.
  #Do we need to clean up afterwards?
end

Given(/^I am on my Trill homepage$/) do
  pending # Write code here that turns the phrase above into concrete actions
  #URL for homepage is required?
  #What provisioning is required?
  #Identify object on homepage to prove test correct.
end



When(/^I login into Trill$/) do
  pending # Write code here that turns the phrase above into concrete actions
  #NFA - Poss Sprint 2
end

When(/^I click on a GDS skill group$/) do
  pending # Write code here that turns the phrase above into concrete actions
  #How do we identify the object ie: Is there a tag?
  #Can we find text or can we find attributes for text?
end

When(/^I click on an expanded GDS skill group$/) do
  pending # Write code here that turns the phrase above into concrete actions
  #How do we identify the object ie: Is there a tag?
  #How do we identify it has collapsed ie: can we no longer find text on page?
  #Can we find attributes for the object?
end



Then(/^I should go to my Trill homepage$/) do
  pending # Write code here that turns the phrase above into concrete actions
  #How do we know that this is the Trill homepage ie:Welcome message?
end

Then(/^I should see my first name$/) do
  pending # Write code here that turns the phrase above into concrete actions
  #Is this information held in a single object and is this object tagged?
end

Then(/^I should see my surname$/) do
  pending # Write code here that turns the phrase above into concrete actions
  #Is this information held in a single object and is this object tagged?
end

Then(/^I should see my role$/) do
  pending # Write code here that turns the phrase above into concrete actions
  #Is this information held in a single object and is this object tagged?
end

Then(/^I should not see my role$/) do
  pending # Write code here that turns the phrase above into concrete actions
  #Is this information held in a single object and is this object tagged?
end

Then(/^I should see my GDS Skills Title$/) do
  pending # Write code here that turns the phrase above into concrete actions
  #Is this information held in a single object and is this object tagged?
end

Then(/^I should not see my GDS Skills Title$/) do
  pending # Write code here that turns the phrase above into concrete actions
  #Can user have no skill ie: set to nil/null?
end

Then(/^I should see my relevant GDS Skill groups$/) do
  pending # Write code here that turns the phrase above into concrete actions
  #Is this information held in a single object and is this object tagged?
  #How many skill groups?
  #How is this displayed and how to test ie: Skill 1/Skill 2 etc?
end

Then(/^the skill group should expand$/) do
  pending # Write code here that turns the phrase above into concrete actions
  #See 'When' statement above.
end

Then(/^I should see the additional skill group information relevant to my role$/) do
  pending # Write code here that turns the phrase above into concrete actions
  #See 'When' statement above.
end

Then(/^the skill group should collapse$/) do
  pending # Write code here that turns the phrase above into concrete actions
  #See 'When' statement above.
end

Then(/^I should not see the additional skill group information relevant to my role$/) do
  pending # Write code here that turns the phrase above into concrete actions
  #See 'When' statement above.
end