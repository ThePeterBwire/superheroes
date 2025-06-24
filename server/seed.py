from random import choice as rc
from app import app, Hero, Power, HeroPower, db

def seed_database():
    print("🚀 Starting database seeding...")
    with app.app_context():
        try:
            print("🧹 Clearing existing data...")
            db.drop_all()
            db.create_all()

            print("⚡ Seeding powers...")
            powers = [
                Power(name="super strength", description="gives the wielder super-human strengths (20+ chars)"),
                Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed"),
                Power(name="super human senses", description="allows the wielder to use senses at super-human level"),
                Power(name="elasticity", description="can stretch the human body to extreme lengths (20+ chars)")
            ]
            db.session.add_all(powers)

            print("🦸 Seeding heroes...")
            heroes = [
                Hero(name="Kamala Khan", super_name="Ms. Marvel"),
                Hero(name="Doreen Green", super_name="Squirrel Girl"),
                Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
                Hero(name="Janet Van Dyne", super_name="The Wasp"),
                Hero(name="Wanda Maximoff", super_name="Scarlet Witch"),
                Hero(name="Carol Danvers", super_name="Captain Marvel"),
                Hero(name="Jean Grey", super_name="Dark Phoenix"),
                Hero(name="Ororo Munroe", super_name="Storm"),
                Hero(name="Kitty Pryde", super_name="Shadowcat"),
                Hero(name="Elektra Natchios", super_name="Elektra")
            ]
            db.session.add_all(heroes)

            print("🔗 Creating hero-power relationships...")
            strengths = ["Strong", "Weak", "Average"]
            for hero in heroes:
                db.session.add(HeroPower(
                    hero=hero,
                    power=rc(powers),
                    strength=rc(strengths)
                ))

            db.session.commit()
            print("🎉 Seeding completed successfully!")
        except Exception as e:
            db.session.rollback()
            print(f"❌ Error: {str(e)}")
            raise

if __name__ == '__main__':
    seed_database()